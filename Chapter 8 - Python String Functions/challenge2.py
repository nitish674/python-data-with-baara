data = "968-Maria, ( D@t@ Engineer ) ;; 27y   "
# clean the string 
processed_data= data.strip().lower().replace("@","a").replace(";","").replace("(","").replace(")","").replace(",","").replace("  "," | ")
print(processed_data)