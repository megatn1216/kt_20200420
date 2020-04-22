var list = [0,1,2,3,4,5,6,7,8,9];
var number = [];

var log='-------------------------------<br>';


if (confirm('야구 게임을 시작할까요?') == true){
    for(var i = 0; i < 3; i++) {
        var select = Math.floor(Math.random() * list.length);
        number[i] = list.splice(select,1)[0];
    }

    var count = 0;
    var strike = 0;
    var ball = 0;
    var error = 0;

    // alert("답 :"+number[0]+number[1]+number[2]);

    while (count < 10) {
        var input = prompt('어디 한번 맞춰보세요! 기회는'+(10-count)+"번 남았습니다"); 
        log = log.concat((count+1) + '번째 입력 숫자 : '+input+"<br>");
        var inputArray = input.split(''); 
        console.log(input);

        strike = 0; 
        ball = 0;
        count++;
        
        if(input === 'undefined') break; //취소 눌렀을시 종료;

        
        // 입력받은 숫자를 비교분석하는 부분
        for (var j = 0; j < 3; j++) {
            for (var k = 0; k < 3; k++) {
                if (number[j] == inputArray[k]) {
                    if (j === k) {
                    strike++;
                    } else {
                    ball++;
                    }
                    break;
                }
            }
        }
        

        // 결과를 표시하는 부분
        if (strike === 3) {
            alert('홈런!!! ' + (count) + '번 만에 성공!!!');
            log = log.concat(count + '번째 입력 결과 : 홈런!!!<br>');
            break;
        } else if (count >= 10) {
            alert('GAME OVER!');
            log = log.concat(count +'번째 입력 결과 : GAME OVER!<br>');
        } else {
            alert(inputArray.join('') + ' : ' + strike + '스트라이크 ' + ball + '볼 !!');
            log = log.concat(count+'번째 입력 결과 : ' + strike + '스트라이크 ' + ball + '볼<br>');
        }
    }

    log = log.replace(",","");
    // alert(log);
    log = log.concat('-------------------------------<br><br>');
    document.getElementById("text1").value = log;
}
