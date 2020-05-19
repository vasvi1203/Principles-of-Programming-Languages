/*To simulate air flight management system using Prolog.*/ 

city(toronto,'$50','60m').
city(london,'$75','80m').
city(paris,'$50','60m').
city(toulouse,'$40','30m').
city(barcelona,'$40','30m').
city(madrid,'$75','45m').
city(valencia,'$40','20m').
city(malaga,'$50','30m').

route(toronto,london,'Air Canada',500,'360m').
route(toronto,london,'United',650,'420m').
route(toronto,madrid,'Air Canada',900,'480m').
route(toronto,madrid,'United',950,'540m').
route(toronto,madrid,'Iberia',800,'480m').

route(madrid,barcelona,'Air Canada',100,'60m').
route(madrid,barcelona,'Iberia',120,'65m').
route(madrid,valencia,'Iberia',40,'50m').
route(madrid,malaga,'Iberia',80,'120m').

route(barcelona,london,'Iberia',220,'240m').
route(barcelona,valencia,'Iberia',110,'75m').

route(valencia,malaga,'Iberia',80,'120m').

route(paris,toulouse,'United',35,'120m').

/* Airport query */
airport(X,Y,Z) :- city(X,Y,Z).

/* Flight query */
flight(A,B,C,D,E) :- route(A,B,C,D,E).

/* (a) Is there a flight from Toronto to Madrid? */
a(A,B) :- route(A,B,C,D,E);route(B,A,C,D,E).

/* (b) A flight from city A to city B with airline C is cheap if its price is less than $ 400. */
b(A,B,C,D,E) :- (route(A,B,C,D,E);route(B,A,C,D,E)),D<400.

/* (c) Is it possible to go from Toronto to Paris in two flights? */
c(X,Y) :- (route(X,Z,A,B,C);route(Z,X,A,B,C)),(route(Y,Z,D,E,F);route(Z,Y,D,E,F)).

/* (d) A flight from city A to city B with airline C is preferred if it's cheap or it's with Air Canada */
d(A,B,C,D,E) :- b(A,B,C,D,E);((flight(A,B,'Air Canada',F,G);flight(B,A,'Air Canada',F,G)),(flight(A,B,C,D,E);flight(B,A,C,D,E)),D<F).

/* (e) If there is a flight from city A to city B with United, then there is a flight from city A to city B with Air Canada. */
e(A,B) :- (flight(A,B,'United',D,E);flight(B,A,'United',D,E)),(flight(A,B,'Air Canada',F,G);flight(B,A,'Air Canada',F,G)).








