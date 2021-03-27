import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int D=sc.nextInt();
        int I=sc.nextInt();
        int S=sc.nextInt();
        int V=sc.nextInt();
        int F=sc.nextInt();

        int arr[][]=new int[I][I];
        String streets[][]=new String[I][I];
        for(int i=0;i<I;i++){
            for(int j=0;j<I;j++){
                arr[i][j]=0;
            }
        }

      //  ArrayList<Integer> streets[] = new ArrayList[S];

        for(int i=0;i<S;i++){
            int s=sc.nextInt();
            int d=sc.nextInt();
            streets[s][d]=sc.next();
            arr[s][d]=sc.nextInt();
        }

       /* ArrayList<Integer> cars[] = new ArrayList[V];


        for(int i=0;i<V;i++){
            cars[i]=new ArrayList<>();
            int c=sc.nextInt();
            for(int j=0;j<c;j++){
                int des=sc.nextInt();
                cars[i].add( map.get(des)[1] );
                streets[des].add(i);
            }
        }*/

       int c=0;
        for(int i=0;i<I;i++){
            boolean flag=false;
            for(int j=0;j<I;j++){
                if(arr[j][i]!=0) flag=true;
            }
            if(flag) c++;
        }
        System.out.println(c);

        for(int i=0;i<I;i++){
            int inc=0;
            List<Integer> list=new ArrayList<>();
            for(int j=0;j<I;j++){
                if(arr[j][i]!=0){
                    inc++;
                    list.add(j);
                }
            }
            if(inc>0){
                System.out.println(i);
                System.out.println(inc);
                Random r=new Random();
                for(int k=0;k<inc;k++){
                    System.out.println(streets[list.get(k)][i]+" "+ (r.nextInt(D-1)+1));
                }
            }
        }
    }
}