//===============================================
// CS:5810 Formal Methods in Software Engineering
// Fall 2015
//
// Homework 3
//
// Name(s):  
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
  requires // (precondition)
  ensures // (postcondition)
{
  l := 0 ;
  while // (guard)
    invariant // (invariant)
    decreases // (variant)
  {
    l := l + 1 ;
  }
}

//===========
// Problem 2
//===========

method closestValue(a: array<int>, k: int) returns (p: nat)
{

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

function maxUpTo(a:array<int>, n:nat):int
{

}

function minUpTo(a:array<int>, n:nat):int
{

}

method range(a:array<int>) returns (r:int)
{
  var min := a[0];
  var max := a[0];
  var i:nat := 1;

  while (i < a.Length)
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

method filter(a:array<int>) returns (b:array<int>, n:nat)
{
	var i: nat := 0;
	n := 0;
  b := new int[a.Length];
 
	// Copy in b all and only the positive elements of a
	while (i < a.Length)
	{
	  if (a[i] > 0) 
	  { 
	    b[n] := a[i];
	    n := n + 1;
	  }
	  i := i + 1;
	}
}


