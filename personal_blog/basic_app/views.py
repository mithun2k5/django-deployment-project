from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from netaddr import *
import re
import datetime
import pytz
from ipwhois import IPWhois

def whois(request):
    form = forms.FormName5()
    global ip_add

    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName5(request.POST)

        if form.is_valid():

            ip_add = request.POST.get('IPv4_Address','')

            return form_name_view6(request)

    return render(request,"new.html",{'form':form})


def decimaltobinary(request):
    form = forms.FormName4()
    global decimal1

    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName4(request.POST)

        if form.is_valid():

            decimal1 = request.POST.get('Decimal_value','')

            return form_name_view5(request)

    return render(request,"decimaltobinary.html",{'form':form})

def binarytodecimal(request):
    form = forms.FormName3()
    global binary1

    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName3(request.POST)

        if form.is_valid():

            binary1 = request.POST.get('Binary_value','')

            return form_name_view4(request)

    return render(request,"binarytodecimal.html",{'form':form})

def changereturn(request):
    form = forms.FormName2()
    global cost1,money1

    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName2(request.POST)

        if form.is_valid():

            cost1 = request.POST.get('cost','')
            money1 = request.POST.get('money','')

            return form_name_view3(request)

    return render(request,"changereturn.html",{'form':form})

def timezoneconversion(request):
    form = forms.FormName1()
    global datetime1, timezone, timezone1

    if request.method == 'POST':
        form = forms.FormName1(request.POST)

        if form.is_valid():

            datetime1 = request.POST.get('Date_and_Time','')
            timezone = request.POST.get('Given_Time_zone','')
            timezone1 = request.POST.get('New_Time_zone','')

            return form_name_view2(request)

    return render(request,"timezoneconversion.html",{'form':form})


def post1(request):
    return render(request,"post1.html")

def post2(request):
    return render(request,"post2.html")

def post3(request):
    return render(request,"post3.html")

def index(request):
    return render(request,"index.html")

def subnetcalculator(request):
    form = forms.FormName()
    global network, host_num1

    if request.method == 'POST':

        form = forms.FormName(request.POST)

        if form.is_valid():

            network = request.POST.get('IP_Address_Block','')
            host_num1 = request.POST.get('Number_of_host_per_subnet','')

            return form_name_view1(request)

    return render(request,"IPv4subnetcalculator.html",{'form':form})

def home(request):
    return render(request,"home.html")

def blog(request):
    return render(request,"blog.html")

def education(request):
    return render(request,"education.html")

def experience(request):
    return render(request,"experience.html")

def certifications(request):
    return render(request,"certification.html")

def skill(request):
    return render(request,"skill.html")

def activities(request):
    return render(request,"activities.html")

def projects(request):
    return render(request,"projects.html")

def project1(request):
    return render(request,"project1.html")

def project2(request):
    return render(request,"project2.html")

def project3(request):
    return render(request,"project3.html")

def project4(request):
    return render(request,"project4.html")

def form_name_view6(request):
    new_form = whois_tool(ipaddress = ip_add)
    return render(request,'new1.html',{'new_form' : new_form})

info = ""

def whois_tool(ipaddress):
    global info
    info = "IP address : " + ipaddress

    try:
        obj = IPWhois(ipaddress)
        results = obj.lookup_whois()
        description = results['nets'][0]['description']
        name = results['nets'][0]['name']
        country = results['nets'][0]['country']
        city = results['nets'][0]['city']
        CIDR = results['nets'][0]['cidr']
        asn_number = results['asn']
        asn_country_code = results['asn_country_code']
        emails = results['nets'][0]['emails']

        text1 = "Description: " + str(description)
        text2 = "Company Name: " + str(name)
        text3 = "Country: " + str(country)
        text4 = "City: " + str(city)
        text5 = "CIDR: " + str(CIDR)
        text6 = "ASN Number: " + str(asn_number)
        text7 = "ASN Country Code: " + str(asn_country_code)
        text8 = "Email Address: " + str(emails)

        return info,text1,text2,text3,text4,text5,text6,text7,text8

    except Exception as e:
        error_message = str(e)
        return info,error_message


def form_name_view5(request):
    new_form = binary_converter(decimal2 = decimal1)
    return render(request,'new1.html',{'new_form' : new_form})


def form_name_view4(request):
    new_form = decimal_converter(binary = binary1)
    return render(request,'new1.html',{'new_form' : new_form})

def binary_converter(decimal2):
    decimal = int(decimal2)
    value = ""
    while (decimal > 1):
        value = value + str(decimal % 2)
        decimal = int(decimal/2)
    if decimal == 0:
        value = value + str(decimal)
    elif decimal == 1:
        value = value + str(decimal)
    new_value = value[::-1]
    value1 = "Binary value is:: " + new_value
    value1 = (value1,)
    return value1

def decimal_converter(binary):
    if len(binary) == 1:
        return int(binary)
    else:
        value = ""
        str_value = " ".join(binary)
        new_value = str_value.split()
        length=len(new_value)
        value=0
        i=0
        while (length>0):
            value = value + (int(new_value[i])*pow(2,length-1))
            i = i + 1
            length = length -1
    value = "Decimal valus is :: " + str(value)
    value = (value,)
    return value

def form_name_view3(request):
    new_form = change_return(cost2 = cost1, money2=money1)
    return render(request,'new1.html',{'new_form' : new_form})

def change_return(cost2,money2):

    cost2 = round(float(cost2),2)
    money2 = round(float(money2),2)

    return_amount = money2 - cost2
    return_amount1 = return_amount
    penny = .01
    nickel = .05
    dime = .1
    quarter = 0.25
    dollar = 1.0
    dollar_number = 0
    quarter_number = 0
    dime_number = 0
    nickel_number = 0
    penny_number = 0
    if (return_amount >= dollar):
        dollar_number = int(return_amount)/1
        return_amount = return_amount%1
    if (return_amount >= 0.25):
        quarter_number = int(return_amount/0.25)
        return_amount = round(return_amount - (0.25*quarter_number),2)
    if (return_amount >= 0.10 ):
        dime_number = int(return_amount/0.1)
        return_amount = round(return_amount - (0.1*dime_number),2)
    if (return_amount >= 0.05):
        nickel_number = int(return_amount/0.05)
        return_amount = round(return_amount - (0.05*nickel_number),2)
    if (return_amount >= 0.01):
        penny_number = int(return_amount/0.01)

    change_return_amount =  "Change Return Amount:: " + str(return_amount1) + " dollar"
    dollar_number =  "Number of Dollar:: " + str(dollar_number)
    quarter_number =  "Number of Quarter:: " + str(quarter_number)
    dime_number = "Number of Dime:: " + str(dime_number)
    nickel_number = "Number of Nickel:: " + str(nickel_number)
    penny_number = "Number of Penny:: " + str(penny_number)

    return change_return_amount,dollar_number,quarter_number,dime_number,nickel_number,penny_number


def form_name_view2(request):
    new_form = timezone_conversion(datetime_given = datetime1, new_timezone=timezone, new_timezone1=timezone1)
    return render(request,'new1.html',{'new_form' : new_form})

def timezone_conversion(datetime_given,new_timezone,new_timezone1):
    global eastern,pacific,central,india,japan,taiwan,utc,bangladesh,korea,singapore
    global australia,indonesia,brazil,london,france,amsterdam,frankfurt,ireland,hong_kong

    global eastern_time,pacific_time,central_time,india_time,japan_time,taiwan_time,utc_time
    global bangladesh_time,korea_time,singapore_time,australia_time,indonesia_time,brazil_time
    global london_time,france_time,amsterdam_time,frankfurt_time,ireland_time,hong_kong_time

    eastern = pytz.timezone('US/Eastern') #est
    pacific = pytz.timezone('US/Pacific') #pst
    central = pytz.timezone('US/Central') #cst
    india = pytz.timezone('Asia/Kolkata') #ist
    japan = pytz.timezone('Asia/Tokyo') #jst
    taiwan = pytz.timezone('Asia/Taipei') #tst
    bangladesh = pytz.timezone('Asia/Dhaka') #bast
    korea = pytz.timezone('Asia/Seoul') #kst
    singapore = pytz.timezone('Asia/Singapore') #sst
    australia = pytz.timezone('Australia/Melbourne') #ast
    indonesia = pytz.timezone('Asia/Jakarta') #idst
    brazil = pytz.timezone('America/Sao_Paulo') #bst
    london = pytz.timezone('Europe/London') #lst
    france = pytz.timezone('Europe/Paris') #fst
    amsterdam = pytz.timezone('Europe/Amsterdam') #amst
    frankfurt = pytz.timezone('Europe/Berlin') #gst
    ireland = pytz.timezone('Europe/Dublin') #irst
    hong_kong = pytz.timezone('Asia/Hong_Kong') #hkt
    utc = pytz.utc #utc

    year = int(datetime_given.split()[0])
    month = int(datetime_given.split()[1])
    date = int(datetime_given.split()[2])
    hour = int(datetime_given.split()[3])
    minute = int(datetime_given.split()[4])

    fmt = '%Y-%m-%d %H:%M  %Z%z'

    def timezone_func(time, time1):
        global eastern,pacific,central,india,japan,taiwan,utc,bangladesh,korea,singapore
        global australia,indonesia,brazil,london,france,amsterdam,frankfurt,ireland,hong_kong

        global eastern_time,pacific_time,central_time,india_time,japan_time,taiwan_time,utc_time
        global bangladesh_time,korea_time,singapore_time,australia_time,indonesia_time,brazil_time
        global london_time,france_time,amsterdam_time,frankfurt_time,ireland_time,hong_kong_time


        eastern_time = time.astimezone(eastern).strftime(fmt)
        pacific_time = time.astimezone(pacific).strftime(fmt)
        central_time = time.astimezone(central).strftime(fmt)
        india_time = time.astimezone(india).strftime(fmt)
        japan_time = time.astimezone(japan).strftime(fmt)
        taiwan_time = time.astimezone(taiwan).strftime(fmt)
        utc_time = time.astimezone(utc).strftime(fmt)
        bangladesh_time = time.astimezone(bangladesh).strftime(fmt)
        korea_time = time.astimezone(korea).strftime(fmt)
        singapore_time = time.astimezone(singapore).strftime(fmt)
        australia_time = time.astimezone(australia).strftime(fmt)
        indonesia_time = time.astimezone(indonesia).strftime(fmt)
        brazil_time = time.astimezone(brazil).strftime(fmt)
        london_time = time.astimezone(london).strftime(fmt)
        france_time = time.astimezone(france).strftime(fmt)
        amsterdam_time = time.astimezone(amsterdam).strftime(fmt)
        frankfurt_time = time.astimezone(frankfurt).strftime(fmt)
        ireland_time = time.astimezone(ireland).strftime(fmt)
        hong_kong_time = time.astimezone(hong_kong).strftime(fmt)

        if time1.lower() == 'est':
            new_eastern = 'Eastern Time:' + str(eastern_time)
            new_eastern = (new_eastern,)
            return new_eastern

        elif time1.lower() == 'pst':
            new_pacific = 'Pacific Time: ' + str(pacific_time)
            new_pacific = (new_pacific,)
            return new_pacific

        elif time1.lower() == 'cst':
            new_central = 'Central Time: ' + str(central_time)
            new_central = (new_central,)
            return new_central

        elif time1.lower() == 'ist':
            new_india = 'India Time: ' + str(india_time)
            new_india = (new_india,)
            return new_india

        elif time1.lower() == 'jst':
            new_japan = 'Japan Time: ' + str(japan_time)
            new_japan = (new_japan,)
            return new_japan

        elif time1.lower() == 'tst':
            new_taiwan = 'Taiwan Time: ' + str(taiwan_time)
            new_taiwan = (new_taiwan,)
            return new_taiwan

        elif time1.lower() == 'utc':
            new_utc = 'UTC Time: ' + str(utc_time)
            new_utc = (new_utc,)
            return new_utc

        elif time1.lower() == 'bast':
            new_bangladesh = 'Bangladesh Time: ' + str(bangladesh_time)
            new_bangladesh =(new_bangladesh,)
            return new_bangladesh

        elif time1.lower() == 'kst':
            new_korea = 'Korea Time: ' + str(korea_time)
            new_korea = (new_korea,)
            return new_korea

        elif time1.lower() == 'sst':
            new_singapore = 'Singapore Time: ' + str(singapore_time)
            new_singapore = (new_singapore,)
            return new_singapore

        elif time1.lower() == 'ast':
            new_australia = 'Australia Time: ' + str(australia_time)
            new_australia = (new_australia,)
            return new_australia

        elif time1.lower() == 'idst':
            new_indonesia = 'Indonesia Time: ' + str(indonesia_time)
            new_indonesia = (new_indonesia,)
            return new_indonesia

        elif time1.lower() == 'bst':
            new_brazil = 'Brazil Time: ' + str(brazil_time)
            new_brazil = (new_brazil,)
            return new_brazil

        elif time1.lower() == 'lst':
            new_london = 'London Time: ' + str(london_time)
            new_london = (new_london,)
            return new_london

        elif time1.lower() == 'fst':
            new_france = 'France Time: ' + str(france_time)
            new_france = (new_france,)
            return new_france

        elif time1.lower() == 'amst':
            new_amsterdam = 'Amsterdam Time: ' + str(amsterdam_time)
            new_amsterdam = (new_amsterdam,)
            return new_amsterdam

        elif time1.lower() == 'gst':
            new_germany = 'Germany Time: ' + str(frankfurt_time)
            new_germany = (new_germany,)
            return new_germany

        elif time1.lower() == 'irst':
            new_ireland = 'Ireland Time: ' + str(ireland_time)
            new_ireland = (ireland_time,)
            return new_ireland

        elif time1.lower() == 'hkt':
            new_hong_kong = 'Hong Kong Time: ' + str(hong_kong_time)
            new_hong_kong = (new_hong_kong,)
            return new_hong_kong

        else:
            text = "Invalid timezone! Please check format as mentioned"
            text = (text,)
            return text

    if new_timezone.lower() == 'est':
        eastern_time = eastern.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=eastern_time,time1=new_timezone1)

    elif new_timezone.lower() == 'pst':
        pacific_time = pacific.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=pacific_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'cst':
        central_time = central.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=central_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'ist':
        india_time = india.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=india_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'jst':
        japan_time = japan.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=japan_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'tst':
        taiwan_time = taiwan.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=taiwan_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'bast':
        bangladesh_time = bangladesh.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=bangladesh_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'kst':
        korea_time = korea.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=korea_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'sst':
        singapore_time = singapore.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=singapore_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'ast':
        australia_time = australia.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=australia_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'idst':
        indonesia_time = indonesia.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=indonesia_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'bst':
        brazil_time = brazil.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=brazil_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'lst':
        london_time = london.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=london_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'fst':
        france_time = france.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=france_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'amst':
        amsterdam_time = amsterdam.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=amsterdam_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'gbt':
        frankfurt_time = frankfurt.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=frankfurt_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'irst':
        ireland_time = ireland.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=ireland_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'hkt':
        hong_kong_time = hong_kong.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=hong_kong_time,time1 = new_timezone1)

    elif new_timezone.lower() == 'utc':
        utc_time = utc.localize(datetime.datetime(year,month,date,hour,minute))
        return timezone_func(time=utc_time,time1 = new_timezone1)

    else:
        text = 'Invalid timezone! Please check format as mentioned'
        text = (text,)
        return text


def form_name_view1(request):
    new_form = subnet_calculator(user_input=network,host=host_num1)
    return render(request,'new1.html',{'new_form':new_form})

def subnet_calculator(user_input,host):

    pattern = '/'

    if re.search(pattern,user_input):

        hosts_per_subnet=int(host)

        net_prefix = int(re.split(pattern,user_input)[1])
        ip_block = re.split(pattern,user_input)[0]

        new_value = int(ip_block.split(".")[0])

        if new_value >=224 and new_value <240 :
            text2 = "This IP block is not usebable as this is a mutlicast block"
            text2 = (text2,)
            return text2

        elif new_value >= 240 and new_value <=255:
            text3 = "This IP block is not useable as this block is reserved for research purpose"
            text3 = (text3,)
            return text3

        elif new_value > 255:
            text4 = "IP block is out of range!!"
            text4 = (text4,)
            return text4

        for value in range(32):
            total_hosts = 2**value


            if hosts_per_subnet < total_hosts:
                bits_needed_for_hosts = value

                interim_value = 32 - bits_needed_for_hosts

                if interim_value - net_prefix < 0:
                    text1 = "IP block will not support that many hosts!!"
                    text1 = (text1,)
                    return text1

                else:
                    borrowed_bits = interim_value - net_prefix
                    Number_of_possible_subnets = 2**borrowed_bits
                    Number_of_possible_hosts_per_subnet = total_hosts - 2
                    subnetwork_mask = ip_block + '/' + str(interim_value)
                    subnetwork_mask_1 = IPNetwork(subnetwork_mask)
                    subnet_mask = subnetwork_mask_1.netmask

                    if IPAddress(ip_block).is_private():
                        text = "This is a private IP block"
                    else:
                        text = "This is a public IP block"


                    new_borrowed_bits = "Bits need to be borrowed from host bit: " + str(borrowed_bits)
                    new_subnets = "Number of possible Subnet: "  + str(Number_of_possible_subnets)
                    new_hosts = "Number of possible hosts per subnet: " + str(Number_of_possible_hosts_per_subnet)
                    new_subnet_mask = "Subnet Mask for each subnet: " + str(subnet_mask)

                ip = IPNetwork(user_input)
                value = ip.subnet(interim_value)
                string = "All Possible subnets: "
                for val in value:
                    string = string + " " + str(val)

                return text,new_borrowed_bits,new_subnets,new_hosts,new_subnet_mask,string

    else:
        text5 = "Invalid Input, please check input as mentioned"
        text5 = (text5,)
        return text5
