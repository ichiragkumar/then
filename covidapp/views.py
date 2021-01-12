from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "5ac49c493emsh40b673f60e7893ap127094jsnd3bde8db50ea",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)
# Create your views here.
def helloworldview(request):
	list1=[]
	noofresults= int(response['results'])
	for x in range(0,noofresults):
		list1.append(response['response'][x]["country"])
	if request.method=="POST":
		noofresults= int(response['results'])
		selectedcountry= request.POST['selectedcountry']		
		for x in range(0, noofresults):
			if selectedcountry== response["response"][x]["country"]:
			   new=response["response"][x]["cases"]["new"]
			   active= response["response"][x]["cases"]["active"]
			   critical= response["response"][x]["cases"]["critical"]
			   recovered= response["response"][x]["cases"]["recovered"]
			   total= response["response"][x]["cases"]["total"]
			   death= int(total)- int(active)- int(recovered)		  
		con = {"selectedcountry":selectedcountry,"list1":list1,"new":new,"active":active,"critical":critical,"recovered":recovered,"total":total,"death":death}
		return render(request,"helloworld.html",con)
	
		list1.append(response['response'][x]["country"])
	context= {"list1":list1}
	#context= {"response": response["results"]}
	return render(request, "helloworld.html", context)

















	#mylistitems= ["member 1", "member 2", "member 3", "member 4", "member 5"]
	#string= "everyone"
	#context= {"mylistitems":mylistitems}
	#return render(request, "helloworld.html", context)