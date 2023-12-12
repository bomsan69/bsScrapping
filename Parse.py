from bs4 import BeautifulSoup as bs
import re

product_list = []


def Parse(html_text):


    soup = bs(html_text, 'html.parser')


    products = soup.select('div.browse-search__pod')

    for product in products:

        itme=[]


        model=product.select_one('div.product-identifier--bd1f5').getText();
        #print(model)
        itme.append(model),

        title=product.select_one('span.product-header__title-product--4y7oa').getText();
        #print(title)
        itme.append(title),

        price=product.select_one('div.price-format__main-price > span:nth-child(2)').getText();
        #print(price)
        itme.append(price),

        #print(price)

        reviews=product.select_one('span.ratings__count--6r7g3').getText();

        pattern = r"\((\d+)\)"

        # 문자열에서 패턴 검색
        match = re.search(pattern, reviews)

        # 저장
        if match:
            reviews = match.group(1)



        #print(reviews)
        itme.append(reviews),


        product_list.append(itme)


    
    
    #print(len(product_list))
    #print(product_list[0])

    return product_list


if __name__ == "__main__":

    result = Parse(open('heom.txt', 'r').read())
    print(result)