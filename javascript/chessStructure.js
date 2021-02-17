var saveVariable = "";
var str = "#"
for(let i=1; i<=8;i++){
    if(i%2!=0){
        for(let j=1;j<=8;j++){
            if(j%2!=0){
                saveVariable+=str;
            }else{
                saveVariable+=" ";
            }   
        }
    }else{
        for(let k=1;k<=8;k++){
            if(k%2!=0){
                saveVariable+=str;
            }else{
                saveVariable+=" ";
            }

        }
    }
   
}
