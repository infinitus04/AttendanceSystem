eMail = "praful@gmail.com"
passWord = "praful1234"

onCheckPass = () =>{

    my=document.getElementsByClassName('form-control') 
    if (my[0].value == "" && my[1].value == ""){


        alert("Please Enter Email Id and Password")
    }
    else if (my[0].value == eMail && my[1].value == passWord){
        alert("Log in Successfull")
    }
    else{
        alert("Invalide Email or Password")
    }
}

// function for log out :- 

logOut = () =>{

    myValue = confirm("Are you sure ?")
    if (myValue == 1){
        alert("Log Out Succesfull")
    }
}

function toggleSelection(row) {
    var rowElement = document.getElementsByTagName("tr")[row];
    rowElement.classList.toggle("selected");
    var checkbox = rowElement.querySelector('input[type="checkbox"]');
    checkbox.checked = !checkbox.checked;
  }

  function updateAttendance(row, present) {
    var rowElement = document.getElementsByTagName("tr")[row];
    rowElement.classList.toggle("selected");
    if (present == 1){
        rowElement.classList.toggle("selected");
    }
  }


  myTable = document.getElementsByClassName("myTableAction") 
  myList = myTable[0].getElementsByTagName("input")
    reverseAll = () => {
        
    //     myBoolx=  confirm("Do you want to clear data ?")
    //     console.log("dodlu")
    //     console.log(myBoolx)
    //   alert(myBoolx)
    //     if(myBoolx == 'true'){

    //     }
    
    for (let index = 0; index < myList.length; index++) {
        myList[index].checked = false
        
        // toggleSelection(index)
        // updateAttendance(index)
        
    }
 

}
submitDone = () => {
    
    let  mySet = []
    
    for (let index = 0; index < myList.length; index++) {
        
        if(  myList[index].checked == false)
        {
            
            //    console.log(index+1)
            mySet.push(index+1)
            //    console.log("done")
        }
        
        
        
        
    }
    if (mySet.length == 0){
       confirm("Do you want to Submit ? \n 0 Students are Absent...") 
    }
    else{
    confirm("Do you want to submit ?" + "\nSr. NO of Absent Students are : "+mySet)
    }
}


window.onload = function() {
    var dateElement = document.getElementById("date");
    var currentDate = new Date();
    dateElement.innerHTML =  currentDate.toDateString();
  };
  
  customAttendance = () => {

    var inputArea = document.getElementById("myCustomInput")
    console.log(inputArea.value)
    let numbers = (inputArea.value).split(",").map(Number); // Convert each string number to an actual number

// Push the numbers into an array
let array = [];
array.push(...numbers);

console.log(array);
console.log(array.length);

if(array[0] == 0){

    alert("Empty Input!!!")
}
else{
for (let index = 0; index < myList.length; index++) {
    myList[index].checked = true
   
    }

array.forEach(element => {
    
    myList[element-1].checked = false
});
}
}