from math import ceil


class Pagination:
    def __init__(self, items:list, page_size = 10) -> object:
        self.items = items
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = ceil(self.items / self.page_size)

    def get_visible_items(self) -> list:
        '''function to see the visiable items of the object'''
        # [a,b,c,d,e,f,g...]      
        start_idx = (self.current_page -1) * self.page_size
        stop_idx = start_idx + self.page_size
        return self.items[start_idx:stop_idx]
    
    def nextPage(self) -> object:
        self.current_page += 1
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")       
p = Pagination(alphabetList, 4)
print(len(p.items))
print(24 // 4)


print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
print(p.current_page)
