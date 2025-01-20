import pandas as pd
from colorama import Fore,Style,Back


class IMDB:
    def showTopList():
        print(Fore.RED,"Top 25 Film".center(70," "))
        df = pd.read_csv("IMDB.csv")[["Title","imdbRating"]].head(25)
        print(Style.BRIGHT,Fore.WHITE,df,Style.RESET_ALL)
        
    def categories():
        print(Fore.RED,"Categories".center(70," "),Style.RESET_ALL)
        print("-Crime\n-Drama\n-Action\n-Biography\n-Adventure\n-Western\n-Comedy\n-Animation\n-Mystery\n-Thriller\n-Horror\n-Family\n-Fantasy\n-Sci-Fi\n-Romance\n-War\n-History\n-Sport\n-Musical\n-Film-Noir")
        inputCat = input("Choose category: ")
        df = pd.read_csv("IMDB.csv")
        mask = df.apply(lambda col: col.astype(str).str.contains(inputCat, na=False)).any(axis=1)
        result = df[mask]["Title"].head(10)
        
        if not result.empty:
            print(Style.BRIGHT,f"\nThese are 10 best movie which I found in the {inputCat} category\n",Style.RESET_ALL)
            print(Fore.YELLOW,result,Fore.WHITE)
        else:
            print("You input wrong category.")

    def searchFilm():
        search = input("Film Name: ")
        df = pd.read_csv("IMDB.csv")
        mask = df['Title'].astype(str).str.contains(search, case=False, na=False)
        result = df[mask][["Title", "Year", "Runtime", "Genre" ,"Director", "imdbRating", "Production"]]
        
        if not result.empty:
            print(Style.BRIGHT,f"\nThese are movies which I found",Style.RESET_ALL)
            print(Fore.CYAN,f"\n{result}")
        else:
            print(f"You input wrong name or {search} isn't in top 250.")

""" Menu """

while True:
    print(Style.BRIGHT,Fore.WHITE,"Pcmuhendisii IMDB menu".center(50,"_"))
    choose = input("1-Show Top List\n2-Categories\n3-Search Film\n4-Exit\n-> ")
    
    if (choose == "4"):
        break
    elif (choose == "3"):
        IMDB.searchFilm()
    elif (choose == "2"):
        IMDB.categories()
    elif (choose == "1"):
        IMDB.showTopList()