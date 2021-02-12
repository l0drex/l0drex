class Food {
    int size;
    int[] coord = new int[2];

    Food(int size){
        this.size = size;
        coord[0] = ((int)random(30))*20;
        coord[1] = ((int)random(20))*20;
    }
    
    void show(){
        fill(#ff0000);
        strokeWeight(5);
        stroke(12);
        rect(coord[0], coord[1], size, size);
    }
}