import requests
import textwrap
import webbrowser as wb

# headers = {
#     "x-rapidapi-key": "efc1793f25mshe7613cea3afeb19p17e4bfjsn9d8c45ebaeae",
#     "x-rapidapi-host": "imdb8.p.rapidapi.com"
# } Expired token

headers = {
    'x-rapidapi-key': "9b73eee7c8msh1e77dc18e9f567cp16d47djsnb6a1fe88168a",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
}

endpoints = {"movie": "https://vidsrc.to/embed/movie/",
             "tvSeries": "https://vidsrc.to/embed/tv/"}


class Imdb:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def getDescription(id):
        try:
            url = "https://imdb8.p.rapidapi.com/title/v2/get-plot"
            querystring = {"tconst": f"{id}"}

            response = requests.get(url, headers=headers, params=querystring)
            description = response.json()['data']['title']['plot']['plotText']['plainText']

            return description


        except(TypeError, KeyError):
            return "NONE"

    def getId(self):
        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q": f"{self.name}"}

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()['d']

        print(f"Found {len(data)} results:")

        if data:
            for i in range(len(data)):
                try:
                    tId = data[i]['id']
                    print(f'\n{i + 1}. Name: {data[i]["l"]}')
                    print(f'Year: {data[i]['y']}')
                    print(f"Category: {data[i]['qid']}")
                    print(f'Description: {textwrap.fill(self.getDescription(tId), width=128)}')
                except:
                    print("No appropriate data found")


            else:
                idIDX = int(input("\nEnter option number (CATEGORY 'movie' or 'tvSeries ONLY'): "))

                while idIDX > len(data):
                    print("\nInput out of range, please enter again")
                    idIDX = int(input("Enter option (CATEGORY 'movie' or 'tvSeries ONLY'): "))

                parcel = {"ID": data[idIDX - 1]['id'], "CATEGORY": data[idIDX - 1]['qid']}

                return parcel
        else:
            print("No results found\n")
            parcel = {"ID": "NONE", "CATEGORY": "NONE"}
            return parcel


class VidSrc:
    def __init__(self, parcel):
        self.id = parcel["ID"]
        self.category = parcel["CATEGORY"]

    def openUrl(self, url):
        print("\nCopy this link into a browser with an AdBlocker preferably "
              "if it dosen't opens up automatically\n\n" + url)

        wb.open_new_tab(url)

    def runner(self):

        if self.category == "movie":
            url = endpoints["movie"] + self.id
            self.openUrl(url)
            return 1

        elif self.category == "NONE":
            return None

        elif self.category == "tvSeries":
            url = endpoints["tvSeries"] + self.id
            self.openUrl(url)
            return 1

        else:
            print("\nSorry the chosen option isn't a movie or a series but maybe a"
                  " tvSpecial/short/something not available yet. \n")


