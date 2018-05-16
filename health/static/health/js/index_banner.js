$(function () {
    var index=0;
    var timer=null;
    var pic=$("#pic").find("li");
    var num=$("#num").find("li");
    var banner=$(".banner");
    var left=$("#left");
    var right=$("#right");

    //鼠标划在窗口上面，停止计时器
    banner.on("mouseover",function () {
        clearInterval(timer);
    });
    //鼠标离开窗口，开启计时器
    banner.on("mouseout",function () {
        timer=setInterval(run,3000)
    });

    //鼠标划在页签上面，停止计时器，手动切换
    for(var i=0;i<num.length;i++){
        num[i].id=i;
        num[i].onmouseover=function(){
            clearInterval(timer);
            changeOption(this.id);
            }
        }
       //定义计时器
        timer=setInterval(run,3000);
        //封装函数run
        function run(){
            index++;
            if (index>=num.length) {index=0}
                changeOption(index);
            }
        //封装函数changeOption
        function changeOption(curindex){
            for(var j=0;j<num.length;j++){
                $(pic[j]).fadeOut(1000);
                num[j].className="";
             }
            $(pic[curindex]).fadeIn(1000);
            num[curindex].className="active";
            index=curindex;
        }
})