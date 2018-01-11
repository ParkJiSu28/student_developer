python 정리
#python 문자열은 불변!
'learnit' ''learnit" '''learnit''' 가능 결합 복제 가능.
문자 추출 offset. 
letters="abvdasdasttdasa"
letters[0]
'a'
letters[1]
'b'
replace() slice와 같은 문자열함수 사용
name='parkjisu'
name.replace('p','o')
'oarkjisu'
'o'+name[1:]
'oarkjisu'
slice[start:end:step]->[:]처음부터끝 [start:]start offset부터 끝까지 시퀀스를 추출
ex)마지막 세문자 추출 letters=asdasdasdasd  letters[-3:0]  ->'asd'
letters[9:-1] ->'as' letters[9:-2]->'a'  문자열 길이 len(letters)=12.
문자열 나누기 spilt  sting.spilt(인자)
string.startwith(인자) 무엇으로 시작하는지.
string.endswith(인자)무엇으로 끝나는가.
ex) word= 'the'
string.find(word)   string.rfind(word)  string.count(word)  ,
73 ( 처음으로 나오는 오프셋) ,214(마지막으로나오는오프셋) ,몇번나오는지
#리스트와 튜플.
#리스트는 모든것의 시퀀스!!!
#튜플은 불변 튜플은 항목을 할당하고나서,이를 바꿀 수 없다. 

#리스트는 변경가능하다.항목을 할당하고 ,자유롭게 수정하거나 삭제 할 수 있다.내용의 순서가 바뀔 수 있다!!!

empty_list[]

weekday=['Mon','Tue','Wen','Thur','Fri','Sat','Sun']
list('cat')-> ['c','a','t'] 튜플을 리스트로 변환->a_tuple = ('ready','fire','aim') ->list(a_tuple)
문자열과 마찬가지로 오프셋으로 값 추출가능.
>>>small_birds= ['humming','finch']
>>> ext_birds = ['dodo', 'pass', 'norwe']
>>> carol_bird = [2, 'French', 2, 'turtle']
>>> all_birds=[small_birds, ext_birds, carol_bird]
>>> all_birds
>>>[['humming', 'finch'], ['dodo', 'pass', 'norwe'], [2, 'French', 2, 'turtle']]
>>> all_birds[::-1]
>>>[[2, 'French', 2, 'turtle'], ['dodo', 'pass', 'norwe'], ['humming', 'finch']]
>>> all_birds.append('chamsea')#리스트끝에 항목 추가하기#
>>> all_birds
>>>[['humming', 'finch'], ['dodo', 'pass', 'norwe'], [2, 'French', 2, 'turtle'], 'chamsea']
>>> others=['bidulgi','ccachi']
>>> all_birds.extend(others)
>>> all_birds
>>>[['humming', 'finch'], ['dodo', 'pass', 'norwe'], [2, 'French', 2, 'turtle'], 'chamsea', 'bidulgi', 'ccachi']
>>> others.insert(2,'jisu')#원하는 위치에 삽입가능#
>>> others
>>>['bidulgi', 'ccachi', 'jisu']
>>> del others[-1]  #오프셋으로 원하는 위치 삭제#
>>> others
>>>['bidulgi', 'ccachi']
>>> others.remove('ccachi')# 위치나 항목을 모를때 사용#
>>> others
>>>['bidulgi']
#pop()은 리스트에서 항목을 가져오는 동시에 그항목을 삭제한다. 오프셋과 함께pop()을 호출했다면 그 오프셋의 항목이 반환된다. 인자가 없다면 -1을 사용한다 pop(0)은 리스트의 헤드(머리시작)을 반환한다.그리고 pop(0)혹은 pop(-1)은 리스트의 꼬리을 반환한다.
#컴퓨터용어로는 append()로 새로운항목을 끝에 추가한뒤 pop()으로 다시 마지막 항목을 제거한다면 LIFO(후입선출) 스택구현한 것이다. 그리고 pop(0)을 사용했다면 FIFO(선입선출)을 큐를 구현한것이다 .수집한 데이터를 가장오래된것을 먼저 사용하거나 최근것을 먼저 사용할떄 유용하다#
>>> firends = ['daejin', 'gooill', 'seahoon']
>>> seperator = '*'
>>> joined = seperator.join(friends)
>>> joined = seperator.join(firends)
>>> joined
>>> 'daejin*gooill*seahoon'                     # join()을 split()의 반대라고 생각하자#
>>> seperated=joined.split(seperator)
>>> seperated
>>> ['daejin', 'gooill', 'seahoon']
>>> seperated==firends
>>> True
#정렬하기 SORT#
sort():리스트 자체를 내부적으로 정렬한다. 내림차순으로 정렬하고 싶다면sort(reverse=True)한다.
sorted():리스트의 정렬된 복사본을 반환한다.
할당:=,복사:copy()->한리스트를 변수 두곳에 할당했을 경우,한리스트를 변경하면 다른 리스트도변경된다. 따라서 copy를 하면 참조하지않고 자기 자신만의 객체를 가진다.
>>> a=[1,2,3]
>>> b=a.copy()
>>> c=list(a)
>>> d=a[:]
>>> a[0]='integer lists are boring'
>>> b
>>> [1, 2, 3]
>>> c
>>> [1, 2, 3]      #a를 변경하였지만 나머지 b,c,d는 변하지 않았다.#
>>> d
>>> [1, 2, 3]
>>> 튜플은 상수리스트다. 튜플을 정의할떄는 ()괄호가 필요  없다.
>>> lear = 'jisu', 'seahoon', 'jinsu'
>>> a, b, c = lear
>>> a
>>> 'jisu'
>>> b
>>> 'seahoon'
>>> c
>>> 'jinsu'    이와 같이 여러 변수가 할당 가능하다. 이것이 튜플 언패킹(tuple unpacking)이다.
>>> tuple()은 다른객체를 튜플로 만들어준다. 튜플을 사용하는 이유가 뭘까??
>>> -튜플은 더 작은 공간을 사용한다.
- 실수로 튜플의 항목을 손상할 염려가 없다.
- 튜플은 딕셔너리키로 사용할 수 있다.
- 네임드 튜플은 객체의 단순한 대안이 될 수 있다.
- 함수의 인자들을 튜플로 전달된다.

#딕셔너리# 
리스트와 비슷하지만 항목의 순서를 따지지 않는다.오프셋으로 항목을 선택할 수 없다.
대시 값에 상응하는 고유한 키를 지정한다. 이키는 대부분 문자열이지만 불변하는 파이썬의 어떤 타입이 될 수도 있다.딕셔너리키는 반드시 유일해야한다. 같은키를 두번이상사용하면 마지막값이승

>>> lol = [ ['a','b'], ['c', 'd'], ['e', 'f'] ]
>>> dict(lol)
>>> {'a': 'b', 'c': 'd', 'e': 'f'}

>>> lol = [ ['a','b'], ['c', 'd'], ['e', 'f'] ]
>>> dict(lol)
>>> {'a': 'b', 'c': 'd', 'e': 'f'}
>>> pythons = {
>>> ... 'chapman': 'Graham',
>>> ... 'cleese': 'john',
>>> ... 'jones': 'eric',
>>> ... 'plain': 'michael'
>>> ... }
>>> pythons
>>> {'chapman': 'Graham', 'cleese': 'john', 'jones': 'eric', 'plain': 'michael'}
>>> pythons['gilliam'] = 'gerry'

>>> pythons
>>> {'chapman': 'Graham', 'cleese': 'john', 'jones': 'eric', 'plain': 'michael', 'gilliam': 'gerry'}

결합하기.update()

>>> others ={ 'Marx':'Granco', 'Howard':'Moe' }
>>> pythons.update(others)
>>> pythons
>>> {'chapman': 'Graham', 'cleese': 'john', 'jones': 'eric', 'plain': 'michael', 'gilliam': 'gerry', 'Marx': 'Granco', 'Howard': 'Moe'}
>>>
>>> 모든항목삭제하기 pythons.clear()   
>>>
>>> >> pythons.get('Marx', 'Not a python') 키유무 옵션 가능.
>>> >> 'Granco'

모든 키얻기..keys()

>>> pythons.keys()
>>> dict_keys(['chapman', 'cleese', 'jones', 'plain', 'gilliam', 'Marx', 'Howard'])

모든 값 얻기..values()

>>> pythons.values()
>>> dict_values(['Graham', 'john', 'eric', 'michael', 'gerry', 'Granco', 'Moe'])

둘다 얻기.(각각 튜플로 반환)

>>> pythons.items()
>>> dict_items([('chapman', 'Graham'), ('cleese', 'john'), ('jones', 'eric'), ('plain', 'michael'), ('gilliam', 'gerry'), ('Marx', 'Granco'), ('Howard', 'Moe')])

# 셋:값은 벌고 키만 남은 딕셔너리와 같음.



