class MyThread extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) System.out.println(i);
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();
    }
}
