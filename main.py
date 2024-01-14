from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def connect_site(date, route, passengers=1):
    url = 'https://atlasbus.by/Маршруты/'+route+'?date='+date+'&passengers='+str(passengers)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': '*/*'
    }
    
    def get_html(url, headers):
        response = requests.get(url, headers=headers)
        return response
    
    html = get_html(url, headers)
    if html.status_code == 200:
        return(parse_tickets(html))
    else:
        print(url)
        return 'Ошибка подключения'

def parse_tickets(response):
    all_ticket_info = []

    def write_info_ticket(index, ticket):
        info_ticket = {'index': str(index)}

        if ticket[13].text == '':
            info_ticket['free_ticket'] = False
            indexes_to_keep = [3, 4, 5, 6, 10, 11, 12, 14]
        else:
            info_ticket['free_ticket'] = True
            ticket[14] = ticket[14].find_all('p')
            indexes_to_keep = [3, 4, 5, 6, 10, 11, 12, 14, 15, 17]

        ticket_list = [
            ticket[i]
            if not isinstance(ticket[i], str) else ticket[i].strip()
            for i in indexes_to_keep
        ]
        info_ticket.update({
            'date_start': ticket_list[1].text,
            'time_start': ticket_list[0].text,
            'city_start': ticket_list[2].text,
            'place_start': ticket_list[3].text,
            'time_finish': ticket_list[4].text,
            'city_finish': ticket_list[5].text,
            'place_finish': ticket_list[6].text,
        })

        if info_ticket['free_ticket']:
            info_ticket['price'] = [ticket_list[7][0].text, ticket_list[8].text, ticket_list[9].text]
            info_ticket['free_place'] = ticket_list[7][1].text
        else:
            info_ticket['price'] = 'None'
            info_ticket['free_place'] = ticket_list[7].text

        all_ticket_info.append(info_ticket)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите нужные элементы на странице и извлеките информацию
    tickets = soup.find_all('div', class_='MuiGrid-root MuiGrid-container')[2:]

    for index, ticket in enumerate(tickets, start=1):
        ticket_div = ticket.find_all('div')
        write_info_ticket(index, ticket_div)

    return all_ticket_info

@app.route('/endpoint', methods=['GET'])
def handle_request():
    print(request.args)
    param1 = request.args.get('date')
    param2 = request.args.get('passengers')
    param3 = request.args.get('route')
    return connect_site(param1, param2, param3)

if __name__ == '__main__':
    app.run()
