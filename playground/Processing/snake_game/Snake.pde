class Snake{
    
    boolean border, loose = false;

    int size, length = 3, dir, speed = 30;
    color snakecolor = #00ff00;
    int[][] snake;
    int[] coord_prev = new int[2];

    Snake(int size, boolean border){

        this.size = size;
        this.border = border;

        dir = RIGHT;
        this.length = 3;

        snake = new int[length][2];

        snake[0][0] = ((int)random(30))*20;
        snake[0][1] = ((int)random(20))*20;

        for (int i = 1; i < snake.length; i++){
            snake[i][0] = snake[i-1][0] - size;
            snake[i][1] = snake[i-1][1];
        }
    }

    void show(){

        //build snakebody

        for (int i = length-1; i > 0; --i) {
            //if(yum(snake[i])) loose = true;

            snake[i]=snake[i-1];
        }

        //draw the snakebody
        for (int[] coord : snake) {
            //stroke(snakecolor);
            fill(snakecolor);
            rect(coord[0], coord[1], size, size);
        }

        //move
        if (frameCount % speed == 0) {

            switch (dir) {
                case UP:
                    snake[0][1]-=20;
                    break;
                case DOWN:
                    snake[0][1]+=20;
                    break;
                case RIGHT:
                    snake[0][0]+=20;
                    break;
                case LEFT:
                    snake[0][0]-=20;
                    break;
                default:
                    println("not sure what to do now...");
            }

            //border collision
            if (!border){
                if (snake[0][0] >= width) snake[0][0] = 0;
                if (snake[0][1] >= height) snake[0][1] = 0;
                if (snake[0][0] < 0) snake[0][0] = width  - size;
                if (snake[0][1] < 0) snake[0][1] = height - size;
            } else {
                if (snake[0][0] >= width) loose = true;
                if (snake[0][1] >= height) loose = true;
                if (snake[0][0] < 0) loose = true;
                if (snake[0][1] < 0) loose = true;
            }
        }
    }
    
    boolean yum(int[] coord){

        if (snake[0][0] == coord[0] && snake[0][1] == coord[1]){
            length++;

            int[][] temp = new int[snake.length][2];
            for (int i = 0; i < snake.length; ++i) temp[i] = snake[i];

            snake = new int[length][2];
            for (int i = 0; i < temp.length; ++i) snake[i] = temp[i];

            snake[length-1] = snake[length-2];

            return true;
        }
        else return false;
    }

}