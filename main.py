import starter
import file_dir as fd

from multiprocessing import Pool

if __name__ == '__main__': # 셀레니움과 멀티프로세싱 풀을 사용하여 크롤링
    filedir = fd.FileDir()
    product_name_list = [[], [], [], [], [], [], [], []] # 멀티프로세싱으로 작업할 리스트를 8개로 분배
    for i in range(len(filedir.product_name_list)):
        product_name_list[i % 8].append(filedir.product_name_list[i]) # 8로 나눈 나머지(0,1,2,3,4,5,6,7)를 인덱스로 상품명 리스트를 각각 분배하여 추가

    pool = Pool(processes=8) # 8개를 수용할 멀티프로세싱 풀을 생성
    pool.map(starter.Starter, product_name_list) # 작업할 메소드와 리스트를 map 함수를 이용하여 묶음
    pool.close() # 작업이 끝나면 풀 종료
    pool.join()