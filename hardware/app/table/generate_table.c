#include <stdlib.h> 
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

#define SP 2

uint64_t fixed_point2(double data,int length);
uint32_t fixed_point(double data,int length);

uint32_t fixed_point(double data,int length){
    
    uint32_t result = 0;
    
    if(data > 0){
        for(int i=0; i<length; i++){
            data *= 2;
        }
        result = floor(data);
    }
    else{
        data = fabsl(data);
        for(int i=0; i<length; i++){
            data *= 2;
        }
        result = floor(data);
        result = ( result ^ 0xFFFFFFFF );
        result += 1;
    }
    return result;
}
uint64_t fixed_point2(double data,int length){
    
    uint64_t result = 0;
    
    if(data > 0){
        for(int i=0; i<length; i++){
            data *= 2;
        }
        result = floor(data);
    }
    else{
        data = fabsl(data);
        for(int i=0; i<length; i++){
            data *= 2;
        }
        result = floor(data);
        result = ( result ^ 0xFFFFFFFFFFFFFFFF );
        result += 1;
    }
    return result;
}

int sampling(int cnt){
    static int interval1=1024,interval2=32768;
    if (cnt == 0){
        interval1=1024;
        interval2=32768;
    }
    if (cnt<1024 && cnt%SP==0){
        return 1;
    }
    else if (1024<=cnt && cnt<32768 && cnt == interval1){
        interval1 *= 2;
        return 1;
    }
    else if (32768<=cnt && cnt<65536 && cnt == (65536-interval2)){
        interval2 /= 2;
        return 1;
    }
    else return 0;
}


void main(int argc, char *argv[]){ 
    FILE *fp_r,*fp_w;
    double data;
    int cnt=0;
    uint32_t result = 0;
    char read_file[30];
    char file_name[30];
    char str[10];
    if (argc < 2) {
            printf("count!!\n");
            exit(0);
    }
    for(int i=0;i<atoi(argv[1]);i++){
        cnt = 0;
        sprintf(str, "%d", i);
        memset(read_file,0,strlen(read_file));
        memset(file_name,0,strlen(file_name));
        strcat(file_name,"table");	
        strcat(file_name,str);	
        strcat(file_name,".txt");
        strcpy(read_file,"./original/");
        strcat(read_file,file_name);

        if((fp_r = fopen(read_file,"r"))==NULL){
            printf("open file error!!\n");
            exit(0);
        }  

        fp_w = fopen(file_name, "w+");
        if (!fp_w) {
            perror("create file error!!");
            exit(0);
        }
        printf("\n %d.txt ",i);
        while (fscanf(fp_r, "%lg",&data)==1){
            if(sampling(cnt)){
                result = fixed_point(data,12);
                //fixed_point2(data,12);
                fprintf(fp_w,"%u\n",result);
            }
            cnt++;
            data=0;
        }
        fclose(fp_r);
        fclose(fp_w);
    }
}

