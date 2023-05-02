from zad1testy import Node, runtests


def SortH(p,k):
    if k == 0:
        return p
    #tworzymy wartownika
    guard = Node()
    guard.next = p
    p = prev = guard            #chyba dobrze
    q = p.next

    count = 0
    #prev bedzie zawsze o jedno oczko za q
    #przechodzimy naszym q az dojdziemy do k-tej liczby w tablicy
    #nastepnie bedziemy tez przesuwac nasze p bo bedzie wiadomo, że
    #żadna wartosc nie zmieni miejsca o wiecej niż k pozycji
    while q and count < k+1:
        count += 1
        if prev.val and prev.val > q.val:
            #gdy tu wchodzimy to prev przestaje sledzic q i zaczyna jechac od p do q
            #wypinamy q, wskaznik q przestawiamy na nastepny
            inserted = q.val
            prev.next = q.next
            q = prev.next
            old_prev = prev             #moze nie trzeba???
            prev = p
            while prev.next.val < inserted:
                prev = prev.next
            #w tym momencie stare q przypinamy za prev
            new = Node()
            new.val = inserted
            new.next = prev.next
            prev.next = new
            prev = old_prev
        else:
            q = q.next
            prev = prev.next

    if q is None:
        return guard.next

    while q:
        p = p.next
        if prev.val and prev.val > q.val:
            #gdy tu wchodzimy to prev przestaje sledzic q i zaczyna jechac od p do q
            #wypinamy q, wskaznik q przestawiamy na nastepny
            inserted = q.val
            prev.next = q.next
            q = prev.next
            old_prev = prev             #moze nie trzeba???
            prev = p
            while prev.next.val < inserted:
                prev = prev.next
            #w tym momencie stare q przypinamy za prev
            new = Node()
            new.val = inserted
            new.next = prev.next
            prev.next = new
            prev = old_prev
        else:
            q = q.next
            prev = prev.next

    #zwracamy p.next zeby pozbyc sie wartownika
    return guard.next


runtests( SortH )
