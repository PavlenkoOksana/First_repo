SIGNS = ["0", "|", "/", "\\", "/", "\\"]
BODY_PARTS = {index:value for index, value in enumerate(SIGNS)}
FILENAME_MAPPING = {
  5:"D:/Projects/vscode-basics/exercises/hangman/words/5.txt",
  6:"D:/Projects/vscode-basics/exercises/hangman/words/6.txt",
  7:"D:/Projects/vscode-basics/exercises/hangman/words/7.txt"
}
         
GALLOWS = {
0:'''      ______
     |      |
     |     
     |      
     |    
     |     
     |_______
     ''',
1: '''      ______
     |      |
     |      0
     |      
     |    
     |     
     |_______
     ''',
2:'''      ______ 
     |      |
     |      0
     |      |  
     |    
     |     
     |_______
     ''',
3:'''      ______
     |      |
     |      0
     |     /|  
     |    
     |     
     |_______
     ''',
4:'''      ______
     |      |
     |      0
     |     /|\  
     |    
     |     
     |_______
     ''',
5:'''      ______
     |      |
     |      0
     |     /|\  
     |     / 
     |     
     |_______
     ''',
6:'''      ______
     |      |
     |      0
     |     /|\  
     |     / \\
     |     
     |_______
     '''
}
  
         

         