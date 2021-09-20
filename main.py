import os
os.system('clear')
try:    
    from selenium import webdriver
    print("[SUCCESS] imported selenium")
except:
    print("[CRITICAL] Can't import selenium ")
    seleniumcommand = "python3 -m pip install selenium"
    print(f"[Info] Running command '{seleniumcommand}'")
    os.system(seleniumcommand)
    os.system("python3 main.py")

import time
try:    
    from bs4 import BeautifulSoup
    print("[SUCCESS] imported BeautifulSoup")
except:
    print("[CRITICAL] Can't import BeautifulSoup")
    bs4command = "python3 -m pip install bs4"
    print(f"[Info] Running command '{bs4command}'")
    os.system(bs4command)
    os.system("python3 main.py")

try:    
    import xlsxwriter
    print("[SUCCESS] imported XLSXWRITER")
except:
    print("[CRITICAL] Can't import XLSXWRITER")
    xlsxwritercommand = "python3 -m pip install xlsxwriter"
    print(f"[Info] Running command '{xlsxwritercommand}'")
    os.system(xlsxwritercommand)
    os.system("python3 main.py")


config = {
    "defaultCities":"cities.txt",
    "defaultKeywords":"keywords.txt",
    "cities":[],
    "keywords":[]
}



def main():
    print("[TITLE]Google Maps Scrapper")
    print("[*]Press 'y' to use defaults")
    useDefaults = input("[?] Use default files or enter filename[y/*]:")
    if useDefaults.strip() == "y":
        useDefaults = True 
    else:
        useDefaults = False

    if useDefaults == False:
        cities_input = input("[?]Enter Filename for 'cities' :")
        try:
            cities_splitter = cities_input.split('.')[1]
            if cities_splitter == "txt":
                try:
                    cities = open(cities_input,"r")
                    config["cities"].insert(0,cities.readlines())
                    print("[Success]")
                except Exception as e:
                    print("[-] Error: {}".format(e))
                    print("[**] Restarting")
                    time.sleep(2)
                    os.system("python3 main.py")

            else:
                print("[-] Error : Unknown file extention")
                print("[Info] Files needs to be (*.txt) files.")
                print("[**] Restarting...")
                time.sleep(2)
                os.system("python3 main.py")
        except:
            try:
                print(f"[Info] Opening file '{cities_input}.txt'")
                cities = open(f"{cities_input}.txt")
                config["cities"].insert(0,cities.readlines())
                print("[Success]")
                
            except Exception as e:
                print("[-] Error: {}".format(e))
                print("[**] Restarting")
                time.sleep()
                os.system("python3 main.py")



    
        keywords_input = input("[?]Enter Filename for 'keywords' :")
        try:
            keywords_splitter = keywords_input.split('.')[1]
            if keywords_splitter == "txt":
                try:
                    keywords = open(keywords_input,"r")
                    config["keywords"].insert(0,keywords.readlines())
                    print("[Success]")
                except Exception as e:
                    print("[-] Error: {}".format(e))
                    print("[**] Restarting")
                    time.sleep(2)
                    os.system("python3 main.py")

            else:
                print("[-] Error : Unknown file extention")
                print("[Info] Files needs to be (*.txt) files.")
                print("[**] Restarting...")
                time.sleep(2)
                os.system("python3 main.py")
        except:
            try:
                print(f"[Info] Opening file '{keywords_input}.txt'")
                keywords = open(f"{keywords_input}.txt")
                config["keywords"].insert(0,keywords.readlines())
                print("[Success]")
                
            except Exception as e:
                print("[-] Error: {}".format(e))
                print("[**] Restarting")
                time.sleep()
                os.system("python3 main.py")

    else:
        print("[Wait] Getting defaults")
        try:
            cities = open(config["defaultCities"])
            config["cities"].insert(0,cities.readlines())
            citiesOpened=True 
        except:
            citiesOpened=False 
        try:
            keywords = open(config["defaultKeywords"])
            config["keywords"].insert(0,keywords.readlines())
            keywordsOpened=True 
        except:
            keywordsOpened=False 

        if keywordsOpened == False or citiesOpened == False:
            print("[CRITICAL] At least one of the files are missing")
            print("Re-starting...")
            time.sleep(2)
            os.system("python3 main.py")

        if keywordsOpened == True and citiesOpened == True:
            print("[Info] Opened files")


    country = input("[?] Country Name : ")
    print("[Info] You entered '{}'".format(country))
    print(f"[Info] Cities: {len(cities.readlines())}")
    print(f"[Info] Keywords: {len(keywords.readlines())}")
    output_filename = input("[?] Enter the output filename:")
    print(f"[Info] Output will be '{output_filename}.xlsx'")
    chromedriverpath = input("[?]Chrome driver path:")
    print("[Info] Checking the path")
    try:
        test = webdriver.Chrome(chromedriverpath)
        test.quit()
        print("[SUCCESS] Path exists")
    except:
        print("[CRITICAL] Can't find chromedriver just put an existing path")
        print("[Wait] Restarting")
        time.sleep(2)
        os.system('clear')
        os.system("python3 main.py")

    #log
    logus = input("[?] Do you want to see the output[y/*] :")
    if logus.strip() == "y":
        logger = True
    else:
        logger = False

    from selenium.webdriver.chrome.options import Options
    cities = config["cities"][0]
    
    keywords =config["keywords"][0]
    print("[LOG] {}".format(cities))
    print("[LOG] {}".format(keywords))
    with open(f'{output_filename}.xlsx',"w"):
        workbook = xlsxwriter.Workbook(f'{output_filename}.xlsx')
        worksheet = workbook.add_worksheet()

    print(f"[LOG]File Created ({output_filename}.xlsx)")
    output = []
    output.clear()
    for c in cities:
        for k in keywords:
            chrome_options = Options()
            if logger == False:
                chrome_options.add_argument("--headless")
            if logger == True:
                pass
            driver = webdriver.Chrome(chromedriverpath,options=chrome_options)
            url = f"https://www.google.com/maps/search/{f'{c} {k} {country}'.replace(' ','+')}"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source,"html.parser")
            
            all_web_icons = soup.find_all("img")

            for icon in all_web_icons:
                if icon.get('src') == "//maps.gstatic.com/consumer/images/icons/2x/ic_directions_gm_blue_24px.png":
                    if logger == True:
                        my_list = []

                        the_text = icon.parent.parent.parent.parent.parent.parent.parent.find_all("span")
                        my_list.clear()
                        for t in the_text :

                            if t.get_text().strip() != "":
                                print(t.get_text())
                                my_list.insert(0,t.get_text())
                                try:
                                    t.get_text().split('+')[1]
                                    phonenum = t.get_text()
                                except:
                                    pass


                        item_data = {
                            "title":the_text[0].get_text(),
                            "phoneNumber":phonenum,
                            "keyword":k,
                            "city":c,
                            "location":the_text[9].get_text(),
                            "kind":my_list[6],
                            "kind_2":my_list[9]
                        }
                        output.insert(0,item_data)
                        print(item_data)

                        print(my_list)


                            

                        # print(icon.parent.parent.parent.parent.parent.get_text())
                        print("\n\n")

                    if logger == False:
                        my_list = []

                        the_text = icon.parent.parent.parent.parent.parent.parent.parent.find_all("span")
                        my_list.clear()
                        for t in the_text :

                            if t.get_text().strip() != "":
                                #print(t.get_text())
                                my_list.insert(0,t.get_text())
                                try:
                                    t.get_text().split('+')[1]
                                    phonenum = t.get_text()
                                except:
                                    pass


                        item_data = {
                            "title":the_text[0].get_text(),
                            "phoneNumber":phonenum,
                            "keyword":k,
                            "city":c,
                            "location":the_text[9].get_text(),
                            "kind":my_list[6],
                            "kind_2":my_list[9]
                        }
                        output.insert(0,item_data)
                        #print(item_data)

                        #print(my_list)


                            

                        # print(icon.parent.parent.parent.parent.parent.get_text())
                        #print("\n\n")
                    

                    
            driver.quit() 
    print("[LOG] Writing the file")
    worksheet.write("A1","Title")
    worksheet.write("B1","Phone Number")
    worksheet.write("C1","Keyword")
    worksheet.write("D1","City")
    worksheet.write("E1","Location")
    worksheet.write("F1","Kind")
    worksheet.write("G1","Kind-2(for errors)")

    for i in range(len(output)-1):
        worksheet.write(f"A{i+2}",output[i]["title"])
        worksheet.write(f"B{i+2}",output[i]["phoneNumber"])
        worksheet.write(f"C{i+2}",output[i]["keyword"])
        worksheet.write(f"D{i+2}",output[i]["city"])
        worksheet.write(f"E{i+2}",output[i]["location"])
        worksheet.write(f"F{i+2}",output[i]["kind"])
        worksheet.write(f"G{i+2}",output[i]["kind_2"])
    
    workbook.close()

    print("[LOG]Done!")
    print("[MSG] Author:Efe Akaröz")
    

    
main()