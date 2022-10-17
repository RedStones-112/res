var board = Array(Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0));
var tableID = Array(Array("00","01","02","03"),Array("10","11","12","13"),Array("20","21","22","23"),Array("30","31","32","33"));
var score;

// 키보드 입력 처리
document.onkeydown = keyDownEventHandler;
function keyDownEventHandler(e){
    switch(e.keyCode){
        case 38: moveDir(0); break; //up
        case 40: moveDir(1); break; //down
        case 37: moveDir(2); break; //left
        case 39: moveDir(3); break; //right
    }
}
init();
function init(){
    score=0;
    for(var i=0;i<4;i++)
        for(var j=0;j<4;j++)
            board[i][j]=0;
    for(var i=0;i<2;i++){
        var rand = parseInt(Math.random()*16);
        var y = parseInt(rand / 4);
        var x = rand % 4;
        if(board[y][x]==0) board[y][x]=getNewNum();
        else i--;
    }
    update();
}
function update(){//화면 업데이트
    for(var i=0;i<4;i++){
        for(var j=0;j<4;j++){
            var cell = document.getElementById(tableID[i][j]);
            cell.innerHTML = board[i][j]==0?"":board[i][j];
            coloring(cell);
        }
    }
    document.getElementById("score").innerHTML=score;
}
function coloring(cell){
    var cellNum = parseInt(cell.innerHTML);
    switch(cellNum){
        case 0:
        case 2:
            cell.style.color="#684A23";
            cell.style.background="#FBEDDC";
            break;
        case 4:
            cell.style.color="#684A23";
            cell.style.background="#F9E2C7";
            break;
        case 8:
            cell.style.color="#684A23";
            cell.style.background="#F6D5AB";
            break;
        case 16:
            cell.style.color="#684A23";
            cell.style.background="#F2C185";
            break;
        case 32:
            cell.style.color="#684A23";
            cell.style.background="#EFB46D";
            break;
        case 64:
            cell.style.color="#FFFFFF";
            cell.style.background="#EBA24A";
            break;
        case 128:
            cell.style.color="#FFFFFF";
            cell.style.background="#E78F24";
            break;
        case 256:
            cell.style.color="#FFFFFF";
            cell.style.background="#E87032";
            break;
        case 512:
            cell.style.color="#FFFFFF";
            cell.style.background="#E85532";
            break;
        case 1024:
            cell.style.color="#FFFFFF";
            cell.style.background="#E84532";
            break;
        case 2048:
            cell.style.color="#FFFFFF";
            cell.style.background="#E83232";
            break;
        default:
            if(cellNum>2048){
                cell.style.color="#FFFFFF";
                cell.style.background="#E51A1A";
            }
            else{
                cell.style.color="#684A23";
                cell.style.background="#FBEDDC";
            }
            break;
    }
}
function generate(){
    var zeroNum=0;
    for(var i = 0;i<4; i++){//빈자리 개수 확인
        for(var j = 0;j<4; j++){
            if(board[i][j]==0) zeroNum++;
        }
    }
    while(1){//빈자리일경우 "1/빈자리 개수"의 확률로 숫자 배치
        for(var i = 0;i<4; i++){
            for(var j = 0;j<4; j++){
                if(board[i][j]==0){
                    var rand = parseInt(Math.random()*zeroNum);
                    if(rand==0){
                        board[i][j]=getNewNum();
                        return;
                    }
                }
            }
        }
    }
}
function getNewNum(){
    var rand = parseInt(Math.random()*11);// 1/10확률로 4 생성
    if(rand==0) return 4;
    return 2;
}
function moveDir(opt){//
        case 0: move(); break;//up
        case 1: rotate(2); move(); rotate(2); break;//down
        case 2: rotate(1); move(); rotate(3); break;//left
        case 3: rotate(3); move(); rotate(1); break;//right
    }
    update();
}
function rotate(n){//배열 회전
    while(n--){//n 이 0되는동안 반복
        var tempBoard = Array(Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0));
        for(var i=0;i<4;i++) {//기존 배열 복사
            for(var j=0;j<4;j++){
                tempBoard[i][j]=board[i][j];
            }
        }
        for(var i=0;i<4;i++) {//배열 회전 후 보드에 붙여넣기
            for(var j=0;j<4;j++){
                board[j][3-i]=tempBoard[i][j];
            }
        }
    }
}
function move(){
    var isMove=false;
    var isPluse = Array(Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0),Array(0,0,0,0));
    for(var i=1;i<4;i++) {
        for(var j=0;j<4;j++){
            if(board[i][j]==0) continue;//보드가 빈자리면 넘어가기
            var tempY = i-1;
            while(tempY>0 && board[tempY][j]==0) tempY--;//i축에서 0이 아닌 칸이 나올때까지 값에 -1
            if(board[tempY][j]==0){//해당 축이 모드 0인경우
                board[tempY][j]=board[i][j];//해당 칸의 값을 축의 가장 아래로
                board[i][j]=0;//해당 칸의 값을 0으로
                isMove=true;
            }
            else if(board[tempY][j]!=board[i][j]){
                if(tempY+1==i) continue;
                board[tempY][j]=board[i][j];
                board[i][j]=0;
                isMove=true;
            }
            else{
                if(isPluse[tempY][j]==0){
                    board[tempY][j]*=2;
                    score+=board[tempY][j];
                    board[i][j]=0;
                    isPluse[tempY][j]=1;
                    isMove=true;
                }
                else{
                    board[tempY+1][j]=board[i][j];
                    board[i][j]=0;
                    isMoved=true;
                }
            }
        }
    }
    if(isMove) generate();
    else checkGameOver();
}
function getMaxNum(){
    var ret=0;
    for(var i=0;i<4;i++)
        for(var j=0;j<4;j++)
            if(board[i][j]>ret)
                ret=board[i][j];
    return ret;
}

// 게임오버 체크
function checkGameOver(){
    for(var i=0;i<4;i++){
        var colCheck = board[i][0];
        if(colCheck==0) return;
        for(var j=1;j<4;j++){
            if(board[i][j]==colCheck || board[i][j]==0) return;
            else colCheck = board[i][j];
        }
    }
    for(var i=0;i<4;i++){
        var rowCheck = board[0][i];
        if(rowCheck==0) return;
        for(var j=1;j<4;j++){
            if(board[j][i]==rowCheck || board[j][i]==0) return;
            else rowCheck = board[j][i];
        }
    }
    gameover();
}

// 게임오버 처리
function gameover(){
    alert("[Game Over]\nMax: "+getMaxNum()+"\nScore"+score);
    init();
}