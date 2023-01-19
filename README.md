# Book CoverPage Design

## AIM:

To design a static web site for a book cover page.

## DESIGN STEPS:
### Step 1:
Clone the github repository into Theia IDE.
### Step 2:
Create a new Django project
### Step 3:
Write the needed HTML code.
### Step 4:
Run the Django server and execute the HTML files.

## PROGRAM :
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Responsive Web Design with HTML5 and CSS</title>
        <style>
        h1{
           color:white;
        }
         .bookpage{
             width: 400px;
             height: 650px;
             background-color: black;
             background-position: center;
             margin-left: auto;
             margin-right: auto ;
             padding: 20px;
             background-image: url('/static/images/dna.jpg');
             background-size: cover;
             background-repeat: no-repeat;
  
         }
         .toptext{
             color:white;
             padding-left: 10px;
             font-size: 14px;
             font-family: Arial, Helvetica, sans-serif;
             
         }
         .tophr{
             color:#e36f2f;
              width: 180px;
         }
         hr{
             color:#e36f2f;
            
         }
         .booktitle{
             font-family: Arial, Helvetica, sans-serif;
             padding: 10px 10px 0px 10px;
             display: flex;
            align-items: center;
            justify-content: center;
  margin-right: 10px;
  margin-left: 10px;
  font-size: 20px;
         }
         .author{
             color:white;
             font-family: Arial, Helvetica, sans-serif;
             display: inline;
             font-size: 24px;
             position:relative;
             line-height: 20px;
              
             
         }
         .sub-text {
             color:white;
             font-family: Arial, Helvetica, sans-serif;
             display: flex;
             line-height: 5px;
            
  margin-right: 10px;
  margin-left: 10px;

  font-size: 14px;
  }
  
.footer {
  color:orange;
  padding-top: 180px;
}
.image {
    color:white;
             font-family: Arial, Helvetica, sans-serif;
 font-size: 22px;
  margin-right: 20px;
}
.bottomhr { 
    color:#e36f2f;
              width: 400px;

}
img {
    width: 90px;
    height: 100px;
    margin-right: 20px;
    vertical-align: bottom;
}
.edition {
    color:#e36f2f;
             font-family: Arial, Helvetica, sans-serif;
 font-size: 22px;
 line-height:bottom;
 
}


        </style>
        </head>
            <body>
                <div class="bookpage">
                    
                    <div class="toptext">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXPERT INSIGHT</div>
                    <div class="tophr"><hr></div> 
               <div class="booktitle"><h1> Responsive Web Design with HTML5 and CSS </h1></div>
               <h3 class="sub-text">Develop future proof responsive websites</h3>
                    <h3 class="sub-text">using latest HTML and CSS designs</h3>
                    <div class="footer">
                        <h2 class="edition">&nbsp;&nbsp;Third 
Edition&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/static/images/author.jpg" alt="Author"></h2>
                      
                        <div class="bottomhr"><hr></div>
                    <div class="author"><h3>&nbsp;&nbsp;Ben Frain &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Packt></h3></div>
                    
                </div>
                </div> 
                
            </body>
        
    
</html>
```

## OUTPUT:
![OUTPUT](./images/book.png)

## Result:
Thus, a static web site for a book cover page is designed and displayed.

