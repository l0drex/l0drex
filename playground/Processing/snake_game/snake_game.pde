int size = 20, score = 0, speed = 500;
boolean border = false;
Food[] apples = new Food[5];
Snake snake = new Snake(size, border);

void setup(){
    size(600, 400);
    for (int i = 0; i < apples.length; ++i) {
        apples[i] = new Food(size);
    }
}

void draw(){

    //delay(speed);
    background(12);
    fill(255);
    textSize(10);
    textAlign(LEFT, TOP);
    text("Score: " + score, 10, 20);

    for (int i = 0; i<apples.length; ++i) {
        apples[i].show();
        if(snake.yum(apples[i].coord)) eat(i);
    }

    snake.show();

    if(snake.loose) endgame();
}

void keyPressed() {
    switch (keyCode) {
        case ESC:
            endgame();
            break;
        case 32: 
            if(looping) noLoop();
            else {
                loop();
                //snake.loose = false;
            }
            break;
        default:
            snake.dir = keyCode;
            break;
    }
}

void eat(int a){
    apples[a] = new Food(size);
    score++;
    if(score % 3 == 0 && snake.speed > 1) snake.speed-=1;
    println(snake.length);
}

void endgame(){
    fill(0, 200);
    rect(0, 0, width, height);

    fill(255);

    textSize(48);
    textAlign(CENTER, CENTER);
    text("You lost!", width/2, height/2-20);

    textSize(20);
    text("Score: " + score, width/2, height/2+20);
    //text("Restart with Space", width/2, height-50);

    noLoop();
}