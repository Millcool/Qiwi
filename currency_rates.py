import requests
import argparse

CBR_API_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

def get_currency_rate(code, date):
    params = {"date_req": date}
    response = requests.get(CBR_API_URL, params=params)

    if response.status_code != 200:
        print("Ошибка при получении данных с сервера ЦБ РФ.")
        return None

    xml_data = response.text
    if code not in xml_data:
        print(f"Курс для валюты с кодом '{code}' не найден на указанную дату '{date}'.")
        return None

    rate_start = xml_data.find(f"<CharCode>{code}</CharCode>") + len(f"<CharCode>{code}</CharCode>")
    rate_end = xml_data.find("</Value>", rate_start)
    rate = xml_data[rate_start:rate_end].replace(",", ".")

    name_start = xml_data.find("<Name>", rate_end) + len("<Name>")
    name_end = xml_data.find("</Name>", name_start)
    name = xml_data[name_start:name_end]

    return name, rate

def main():
    parser = argparse.ArgumentParser(description="Получение курса валют ЦБ РФ за определенную дату.")
    parser.add_argument("--code", type=str, help="Код валюты в формате ISO 4217", required=True)
    parser.add_argument("--date", type=str, help="Дата в формате YYYY-MM-DD", required=True)
    args = parser.parse_args()

    name, rate = get_currency_rate(args.code.upper(), args.date)
    if name and rate:
        print(f"{args.code.upper()} ({name}): {rate}")

if __name__ == "__main__":
    main()
