
def printMovieList():
    file = open("movies.txt", "r")
    movies = file.readlines()
    for i in range(len(movies)):
        print(i+1, movies[i],end="")
    
    print("\n\n")
    movieChoice = int(input("enter your choice: ")) 
    movieName = movies[movieChoice-1]
    #print("you have selected: ", movieName)
    
    movieMetaData = movieName.split(" ")
    selectedMovie = movieMetaData[0]
    movieDuration = movieMetaData[1]
    showTimings = movieMetaData[2].strip("\n")
    
    print("selected movie: ", selectedMovie)
    print("movie duration: ", movieDuration)
    print("show timings: ", showTimings)
    

while True:
    print("1 show movie list")
    print("2 book ticket")
    print("3 download ticket")
    print("4 exit")
    choice = int(input("enter your choice: "))
    
    
    if choice == 1:
        print("show movie list")
        printMovieList()
        print("\n\n")
    elif choice == 2:
        print("book ticket")
    elif choice == 3:
        print("download ticket")
    elif choice == 4:
        print("exit")
        break
            
            
    
    