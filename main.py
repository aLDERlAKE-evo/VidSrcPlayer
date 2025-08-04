import customAPI

imdbRun = None
ID = None


def main():

    name = input("Enter Name of anything you wish to watch: ")

    while name == '':
        print("\nIt seems you have not input anything")
        name = input("Enter Name of anything you wish to watch: ")


    try:
        imdbRun = customAPI.Imdb(name)
        ID = imdbRun.getId()

    except:
        print("\nYou entered an invalid name,\nPlease enter a valid name\n")
        main()

    VidSrcRun = customAPI.VidSrc(ID)
    if VidSrcRun.runner() is None:
        main()

main()