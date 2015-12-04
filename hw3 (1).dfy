//===============================================
// CS:5810 Formal Methods in Software Engineering
// Fall 2015
//
// Homework 3
//
// Name(s):  I-FAN HUANG
//
//===============================================

//===========
// Problem 1
//===========

// Compute 2^k
function method exp2(k: nat): nat
{ 
 if (k == 0) then 1 else 2*exp2(k - 1) 
}
method ilog(n: nat) returns (l: nat)
  requires n != 0
  ensures n > 0
{
  l := 0 ;
  while(l < n)
    invariant 0 <= l <= n
    invariant 0 <= exp2(n) 
    decreases n - l
  {
    l := l + 1 ;
  }
  }

//===========
// Problem 2
//===========

method closestValue(a: array<int>, k: int) returns (p: nat)
  requires a != null;
  requires a.Length > 0;
//  requires forall k ::
  ensures 0 <= p <= a.Length;
//  ensures 0 <= p ==> p < a.Length && a[p] == k 
//  ensures  
//var i := 0;
{
  var i: nat := 0; 
  var low := 0;
  var high := a.Length -1;
  var mid;
while(low <= high)
  invariant 0 <= i <= a.Length;
  {
    mid := (low + high)/2;
    if(mid == 0)
  }
  }


//===========
// Problem 3
//===========

method arrayMax(a: array<int>) returns (a: int)
{

}


//===========
// Problem 4
//===========

function max(first:int, second:int):int
{
  if first > second then first else second
}
function maxUpTo(a:array<int>, n:nat):int
requires a != null;
requires a.Length > 0;
requires 1 <= n <= a.Length;
reads a;
{
  if n == 1 then a[0] else max(a[n-1], maxUpTo(a, n-1))
}
function min(first:int, second:int):int
{
  if first < second then first else second
}
function minUpTo(a:array<int>, n:nat):int
requires a != null;
requires a.Length > 0;
requires 1 <= n <= a.Length;
reads a;
{
  if n == 1 then a[0] else min(a[n-1], minUpTo(a, n-1))
}

method range(a:array<int>) returns (r:int)
requires a != null;
requires a.Length > 1;
ensures r == maxUpTo(a, a.Length) - minUpTo(a, a.Length);
{
  var min := a[0];
  var max := a[0];
  var i:nat := 1;

  while (i < a.Length)
  invariant 1 <= i <= a.Length;
  invariant max == maxUpTo(a, i);
  invariant min == minUpTo(a, i);
  decreases a.Length - i;
  {
    if (min > a[i]) { min := a[i]; }
    if (max < a[i]) { max := a[i]; }
    i := i + 1;
  }
  r := max - min;
}

//===========
// Problem 5
//===========
function numOfPos(a: array<int>, n: nat): nat
requires a != null;
requires a.Length > 0;
requires 0 <= n <= a.Length;
reads a;
{
  if n == 0 then 0 
            else if a[n-1] > 0 then numOfPos(a, n-1) + 1 else numOfPos(a, n-1)
}
//first i elements of A have n postive number and the same as the top n of b in the same order
function PosofA(a : array<int>, b : array<int> , i : nat, n : nat) : bool
requires a != null;
requires b != null;
requires a.Length >0;
requires 0 <= i <= a.Length
requires b.Length > 0;
requires a.Length == b.Length;
requires 0 <= n <= i;
reads a;
reads b;
{
  if i == 0 then if n == 0 then true else false
            else 
            if n == 0 then if numOfPos(a, i) == 0 then true else false
                      else
                      //if in the first i elements of a there are n positive element
                      if numOfPos(a, i) == n then
                                             //if in the first i-1 elements of a there are n-1 positive elements, which means the ith element is positive and 
                                             //it must be the nth element in b
                                             if numOfPos(a, i-1) == n-1 then if a[i-1] == b[n-1] && a[i-1] > 0 then true else false
                                                                        //else if in the first i-1 elements of a there are still n positive elements, this means
                                                                        // the ith elememt is negative which we dont care.
                                                                        else if numOfPos(a, i-1) == n then true else false
                      else false 
}


method filter(a:array<int>) returns (b:array<int>, n:nat)
requires a != null;
requires a.Length > 0;
ensures b != null;
ensures b.Length > 0;
ensures a.Length == b.Length;
ensures n <= a.Length;
ensures forall k :: 0 <= k < n ==> b[k] > 0;
ensures numOfPos(a, a.Length) == n;
//ensure that positive elements in a the same order in b
ensures PosofA(a, b, a.Length, n);
{
	var i: nat := 0;
	n := 0;
  b := new int[a.Length];
 
	// Copy in b all and only the positive elements of a
	while (i < a.Length)
  invariant 0 <= i <= a.Length;
  invariant 0 <= n <= i;
  invariant 0 <= n <= b.Length;
  invariant n == numOfPos(a, i);
  invariant forall k :: 0 <= k < n ==> b[k] > 0;
  invariant PosofA(a, b, i, n);
  
	{
	  if (a[i] > 0) 
	  { 
	    b[n] := a[i];
	    n := n + 1;
	  }
	  i := i + 1;
	}
}
