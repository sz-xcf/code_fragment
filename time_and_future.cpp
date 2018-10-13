#include <future>
#include <iostream>
#include <sys/time.h>
#include <iomanip>


using namespace std;


long long find_the_answer();
void do_other_stuff();
void sysLocalTime(string s);

int	main()
{
        sysLocalTime("main start");
        std::future<long long> the_answer=std::async(launch::async, find_the_answer);
        do_other_stuff();

        std::future_status status;
        do {
                status = the_answer.wait_for(std::chrono::seconds(1));
                if (status == std::future_status::deferred) {
                        std::cout << "deferred\n";
                } else if (status == std::future_status::timeout) {
                        std::cout << "timeout\n";
                } else if (status == std::future_status::ready) {
                        std::cout << "ready!\n";
                }
        } while (status != std::future_status::ready);

        std::cout << "The answer is	" << the_answer.get() << std::endl;

        sysLocalTime("main end");
        return 0;
}


long long find_the_answer(){
        sysLocalTime("find_the_answer start");

        // sleep or do some time consuming things
        //
        // this_thread::sleep_for(chrono::seconds(5));
        //
        long long sum = 0;
        long long times = 70000;
        for (long long i=0; i<times; i++){
                long long part_sum = 0;
                for (long long j=0; j<i; j++){
                        part_sum += j; 
                }

                sum += part_sum;
        }
        sysLocalTime("find_the_answer end");

        return sum;
}

void do_other_stuff(){
        sysLocalTime("do_other_stuff start");
        this_thread::sleep_for(chrono::seconds(2));
        sysLocalTime("do_other_stuff end");
}


void sysLocalTime(string info) 
{ 
        struct timeval    tv; 
        struct timezone tz; 
        struct tm         *p; 


        gettimeofday(&tv, &tz); 
        p = localtime(&tv.tv_sec); 
        cout.fill('.');

        cout << left << setw(30) << info;
        printf(" %04d-%02d-%02d %02d:%02d:%02d.%03ld\n", 
                        1900+p->tm_year, 1+p->tm_mon, p->tm_mday, p->tm_hour, p->tm_min, p->tm_sec, tv.tv_usec/1000);  
}  







