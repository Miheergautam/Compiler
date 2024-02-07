try {
    var a : num;
    take(a);
    show(a);
}
catch(Exception e) {
    show("An exception occurred");
}
finally {
    show("This block always executes");
}


var arr : <num>[5];
arr[0] = 1;
arr[1] = 2;
arr[2] = 3;
arr[3] = 4;
arr[4] = 5;

show(arr[2]);
