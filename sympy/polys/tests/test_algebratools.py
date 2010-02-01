"""Tests for classes defining properties of ground domains, e.g. ZZ, QQ, ZZ[x] ... """

from sympy.polys.algebratools import (
    ZZ, QQ, RR, PolynomialRing, FractionField, EX
)

from sympy.polys.polyerrors import (
    UnificationFailed,
    GeneratorsNeeded,
)

from sympy import S, sqrt, sin, oo, raises

from sympy.abc import x, y

def test_Algebra__unify():
    assert ZZ.unify(ZZ) == ZZ
    assert QQ.unify(QQ) == QQ

    assert ZZ.unify(QQ) == QQ
    assert QQ.unify(ZZ) == QQ

    assert EX.unify(EX) == EX

    assert ZZ.unify(EX) == EX
    assert QQ.unify(EX) == EX
    assert EX.unify(ZZ) == EX
    assert EX.unify(QQ) == EX

    assert ZZ.poly_ring('x').unify(EX) == EX
    assert ZZ.frac_field('x').unify(EX) == EX
    assert EX.unify(ZZ.poly_ring('x')) == EX
    assert EX.unify(ZZ.frac_field('x')) == EX

    assert ZZ.poly_ring('x','y').unify(EX) == EX
    assert ZZ.frac_field('x','y').unify(EX) == EX
    assert EX.unify(ZZ.poly_ring('x','y')) == EX
    assert EX.unify(ZZ.frac_field('x','y')) == EX

    assert QQ.poly_ring('x').unify(EX) == EX
    assert QQ.frac_field('x').unify(EX) == EX
    assert EX.unify(QQ.poly_ring('x')) == EX
    assert EX.unify(QQ.frac_field('x')) == EX

    assert QQ.poly_ring('x','y').unify(EX) == EX
    assert QQ.frac_field('x','y').unify(EX) == EX
    assert EX.unify(QQ.poly_ring('x','y')) == EX
    assert EX.unify(QQ.frac_field('x','y')) == EX

    assert ZZ.poly_ring('x').unify(ZZ) == ZZ.poly_ring('x')
    assert ZZ.poly_ring('x').unify(QQ) == QQ.poly_ring('x')
    assert QQ.poly_ring('x').unify(ZZ) == QQ.poly_ring('x')
    assert QQ.poly_ring('x').unify(QQ) == QQ.poly_ring('x')

    assert ZZ.unify(ZZ.poly_ring('x')) == ZZ.poly_ring('x')
    assert QQ.unify(ZZ.poly_ring('x')) == QQ.poly_ring('x')
    assert ZZ.unify(QQ.poly_ring('x')) == QQ.poly_ring('x')
    assert QQ.unify(QQ.poly_ring('x')) == QQ.poly_ring('x')

    assert ZZ.poly_ring('x','y').unify(ZZ) == ZZ.poly_ring('x','y')
    assert ZZ.poly_ring('x','y').unify(QQ) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x','y').unify(ZZ) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x','y').unify(QQ) == QQ.poly_ring('x','y')

    assert ZZ.unify(ZZ.poly_ring('x','y')) == ZZ.poly_ring('x','y')
    assert QQ.unify(ZZ.poly_ring('x','y')) == QQ.poly_ring('x','y')
    assert ZZ.unify(QQ.poly_ring('x','y')) == QQ.poly_ring('x','y')
    assert QQ.unify(QQ.poly_ring('x','y')) == QQ.poly_ring('x','y')

    assert ZZ.frac_field('x').unify(ZZ) == ZZ.frac_field('x')
    assert ZZ.frac_field('x').unify(QQ) == EX # QQ.frac_field('x')
    assert QQ.frac_field('x').unify(ZZ) == EX # QQ.frac_field('x')
    assert QQ.frac_field('x').unify(QQ) == QQ.frac_field('x')

    assert ZZ.unify(ZZ.frac_field('x')) == ZZ.frac_field('x')
    assert QQ.unify(ZZ.frac_field('x')) == EX # QQ.frac_field('x')
    assert ZZ.unify(QQ.frac_field('x')) == EX # QQ.frac_field('x')
    assert QQ.unify(QQ.frac_field('x')) == QQ.frac_field('x')

    assert ZZ.frac_field('x','y').unify(ZZ) == ZZ.frac_field('x','y')
    assert ZZ.frac_field('x','y').unify(QQ) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(ZZ) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(QQ) == QQ.frac_field('x','y')

    assert ZZ.unify(ZZ.frac_field('x','y')) == ZZ.frac_field('x','y')
    assert QQ.unify(ZZ.frac_field('x','y')) == EX # QQ.frac_field('x','y')
    assert ZZ.unify(QQ.frac_field('x','y')) == EX # QQ.frac_field('x','y')
    assert QQ.unify(QQ.frac_field('x','y')) == QQ.frac_field('x','y')

    assert ZZ.poly_ring('x').unify(ZZ.poly_ring('x')) == ZZ.poly_ring('x')
    assert ZZ.poly_ring('x').unify(QQ.poly_ring('x')) == QQ.poly_ring('x')
    assert QQ.poly_ring('x').unify(ZZ.poly_ring('x')) == QQ.poly_ring('x')
    assert QQ.poly_ring('x').unify(QQ.poly_ring('x')) == QQ.poly_ring('x')

    assert ZZ.poly_ring('x','y').unify(ZZ.poly_ring('x')) == ZZ.poly_ring('x','y')
    assert ZZ.poly_ring('x','y').unify(QQ.poly_ring('x')) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x','y').unify(ZZ.poly_ring('x')) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x','y').unify(QQ.poly_ring('x')) == QQ.poly_ring('x','y')

    assert ZZ.poly_ring('x').unify(ZZ.poly_ring('x','y')) == ZZ.poly_ring('x','y')
    assert ZZ.poly_ring('x').unify(QQ.poly_ring('x','y')) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x').unify(ZZ.poly_ring('x','y')) == QQ.poly_ring('x','y')
    assert QQ.poly_ring('x').unify(QQ.poly_ring('x','y')) == QQ.poly_ring('x','y')

    assert ZZ.poly_ring('x','y').unify(ZZ.poly_ring('x','z')) == ZZ.poly_ring('x','y','z')
    assert ZZ.poly_ring('x','y').unify(QQ.poly_ring('x','z')) == QQ.poly_ring('x','y','z')
    assert QQ.poly_ring('x','y').unify(ZZ.poly_ring('x','z')) == QQ.poly_ring('x','y','z')
    assert QQ.poly_ring('x','y').unify(QQ.poly_ring('x','z')) == QQ.poly_ring('x','y','z')

    assert ZZ.frac_field('x').unify(ZZ.frac_field('x')) == ZZ.frac_field('x')
    assert ZZ.frac_field('x').unify(QQ.frac_field('x')) == QQ.frac_field('x')
    assert QQ.frac_field('x').unify(ZZ.frac_field('x')) == QQ.frac_field('x')
    assert QQ.frac_field('x').unify(QQ.frac_field('x')) == QQ.frac_field('x')

    assert ZZ.frac_field('x','y').unify(ZZ.frac_field('x')) == ZZ.frac_field('x','y')
    assert ZZ.frac_field('x','y').unify(QQ.frac_field('x')) == QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(ZZ.frac_field('x')) == QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(QQ.frac_field('x')) == QQ.frac_field('x','y')

    assert ZZ.frac_field('x').unify(ZZ.frac_field('x','y')) == ZZ.frac_field('x','y')
    assert ZZ.frac_field('x').unify(QQ.frac_field('x','y')) == QQ.frac_field('x','y')
    assert QQ.frac_field('x').unify(ZZ.frac_field('x','y')) == QQ.frac_field('x','y')
    assert QQ.frac_field('x').unify(QQ.frac_field('x','y')) == QQ.frac_field('x','y')

    assert ZZ.frac_field('x','y').unify(ZZ.frac_field('x','z')) == ZZ.frac_field('x','y','z')
    assert ZZ.frac_field('x','y').unify(QQ.frac_field('x','z')) == QQ.frac_field('x','y','z')
    assert QQ.frac_field('x','y').unify(ZZ.frac_field('x','z')) == QQ.frac_field('x','y','z')
    assert QQ.frac_field('x','y').unify(QQ.frac_field('x','z')) == QQ.frac_field('x','y','z')

    assert ZZ.poly_ring('x').unify(ZZ.frac_field('x')) == ZZ.frac_field('x')
    assert ZZ.poly_ring('x').unify(QQ.frac_field('x')) == EX # QQ.frac_field('x')
    assert QQ.poly_ring('x').unify(ZZ.frac_field('x')) == EX # QQ.frac_field('x')
    assert QQ.poly_ring('x').unify(QQ.frac_field('x')) == QQ.frac_field('x')

    assert ZZ.poly_ring('x','y').unify(ZZ.frac_field('x')) == ZZ.frac_field('x','y')
    assert ZZ.poly_ring('x','y').unify(QQ.frac_field('x')) == EX # QQ.frac_field('x','y')
    assert QQ.poly_ring('x','y').unify(ZZ.frac_field('x')) == EX # QQ.frac_field('x','y')
    assert QQ.poly_ring('x','y').unify(QQ.frac_field('x')) == QQ.frac_field('x','y')

    assert ZZ.poly_ring('x').unify(ZZ.frac_field('x','y')) == ZZ.frac_field('x','y')
    assert ZZ.poly_ring('x').unify(QQ.frac_field('x','y')) == EX # QQ.frac_field('x','y')
    assert QQ.poly_ring('x').unify(ZZ.frac_field('x','y')) == EX # QQ.frac_field('x','y')
    assert QQ.poly_ring('x').unify(QQ.frac_field('x','y')) == QQ.frac_field('x','y')

    assert ZZ.poly_ring('x','y').unify(ZZ.frac_field('x','z')) == ZZ.frac_field('x','y','z')
    assert ZZ.poly_ring('x','y').unify(QQ.frac_field('x','z')) == EX # QQ.frac_field('x','y','z')
    assert QQ.poly_ring('x','y').unify(ZZ.frac_field('x','z')) == EX # QQ.frac_field('x','y','z')
    assert QQ.poly_ring('x','y').unify(QQ.frac_field('x','z')) == QQ.frac_field('x','y','z')

    assert ZZ.frac_field('x').unify(ZZ.poly_ring('x')) == ZZ.frac_field('x')
    assert ZZ.frac_field('x').unify(QQ.poly_ring('x')) == EX # QQ.frac_field('x')
    assert QQ.frac_field('x').unify(ZZ.poly_ring('x')) == EX # QQ.frac_field('x')
    assert QQ.frac_field('x').unify(QQ.poly_ring('x')) == QQ.frac_field('x')

    assert ZZ.frac_field('x','y').unify(ZZ.poly_ring('x')) == ZZ.frac_field('x','y')
    assert ZZ.frac_field('x','y').unify(QQ.poly_ring('x')) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(ZZ.poly_ring('x')) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x','y').unify(QQ.poly_ring('x')) == QQ.frac_field('x','y')

    assert ZZ.frac_field('x').unify(ZZ.poly_ring('x','y')) == ZZ.frac_field('x','y')
    assert ZZ.frac_field('x').unify(QQ.poly_ring('x','y')) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x').unify(ZZ.poly_ring('x','y')) == EX # QQ.frac_field('x','y')
    assert QQ.frac_field('x').unify(QQ.poly_ring('x','y')) == QQ.frac_field('x','y')

    assert ZZ.frac_field('x','y').unify(ZZ.poly_ring('x','z')) == ZZ.frac_field('x','y','z')
    assert ZZ.frac_field('x','y').unify(QQ.poly_ring('x','z')) == EX # QQ.frac_field('x','y','z')
    assert QQ.frac_field('x','y').unify(ZZ.poly_ring('x','z')) == EX # QQ.frac_field('x','y','z')
    assert QQ.frac_field('x','y').unify(QQ.poly_ring('x','z')) == QQ.frac_field('x','y','z')

    raises(UnificationFailed, "ZZ.poly_ring('x','y').unify(ZZ, gens=('y', 'z'))")
    raises(UnificationFailed, "ZZ.unify(ZZ.poly_ring('x','y'), gens=('y', 'z'))")

def test_Algebra__contains__():
    ALG = QQ.algebraic_field(sqrt(2)+sqrt(3))

    assert (-7 in ZZ) == True
    assert ( 0 in ZZ) == True
    assert (17 in ZZ) == True

    assert (-7 in QQ) == True
    assert ( 0 in QQ) == True
    assert (17 in QQ) == True

    assert (-7 in RR) == True
    assert ( 0 in RR) == True
    assert (17 in RR) == True

    assert (-7 in ALG) == True
    assert ( 0 in ALG) == True
    assert (17 in ALG) == True

    assert (-7 in ZZ[x,y]) == True
    assert ( 0 in ZZ[x,y]) == True
    assert (17 in ZZ[x,y]) == True

    assert (-7 in QQ[x,y]) == True
    assert ( 0 in QQ[x,y]) == True
    assert (17 in QQ[x,y]) == True

    assert (-7 in RR[x,y]) == True
    assert ( 0 in RR[x,y]) == True
    assert (17 in RR[x,y]) == True

    assert (-S(1)/7 in ZZ) == False
    assert ( S(3)/5 in ZZ) == False

    assert (-S(1)/7 in QQ) == True
    assert ( S(3)/5 in QQ) == True

    assert (-S(1)/7 in RR) == True
    assert ( S(3)/5 in RR) == True

    assert (-S(1)/7 in ALG) == True
    assert ( S(3)/5 in ALG) == True

    assert (-S(1)/7 in ZZ[x,y]) == False
    assert ( S(3)/5 in ZZ[x,y]) == False

    assert (-S(1)/7 in QQ[x,y]) == True
    assert ( S(3)/5 in QQ[x,y]) == True

    assert (-S(1)/7 in RR[x,y]) == True
    assert ( S(3)/5 in RR[x,y]) == True

    assert (oo in ZZ) == False
    assert (oo in QQ) == False
    assert (oo in RR) == False
    assert (oo in ALG) == False
    assert (oo in ZZ[x,y]) == False
    assert (oo in QQ[x,y]) == False
    assert (oo in RR[x,y]) == False

    assert (-oo in ZZ) == False
    assert (-oo in QQ) == False
    assert (-oo in RR) == False
    assert (-oo in ALG) == False
    assert (-oo in ZZ[x,y]) == False
    assert (-oo in QQ[x,y]) == False
    assert (-oo in RR[x,y]) == False

    assert (sqrt(7) in EX) == True
    assert (sqrt(7) in ZZ) == False
    assert (sqrt(7) in QQ) == False
    assert (sqrt(7) in RR) == True
    assert (sqrt(7) in ALG) == False
    assert (sqrt(7) in ZZ[x,y]) == False
    assert (sqrt(7) in QQ[x,y]) == False
    assert (sqrt(7) in RR[x,y]) == True

    assert (2*sqrt(3)+1 in EX) == True
    assert (2*sqrt(3)+1 in ZZ) == False
    assert (2*sqrt(3)+1 in QQ) == False
    assert (2*sqrt(3)+1 in RR) == True
    assert (2*sqrt(3)+1 in ALG) == True
    assert (2*sqrt(3)+1 in ZZ[x,y]) == False
    assert (2*sqrt(3)+1 in QQ[x,y]) == False
    assert (2*sqrt(3)+1 in RR[x,y]) == True

    assert (sin(1) in EX) == True
    assert (sin(1) in ZZ) == False
    assert (sin(1) in QQ) == False
    assert (sin(1) in RR) == True
    assert (sin(1) in ALG) == False
    assert (sin(1) in ZZ[x,y]) == False
    assert (sin(1) in QQ[x,y]) == False
    assert (sin(1) in RR[x,y]) == True

    assert (x**2 + 1 in EX) == True
    assert (x**2 + 1 in ZZ) == False
    assert (x**2 + 1 in QQ) == False
    assert (x**2 + 1 in RR) == False
    assert (x**2 + 1 in ALG) == False
    assert (x**2 + 1 in ZZ[x]) == True
    assert (x**2 + 1 in QQ[x]) == True
    assert (x**2 + 1 in RR[x]) == True
    assert (x**2 + 1 in ZZ[x,y]) == True
    assert (x**2 + 1 in QQ[x,y]) == True
    assert (x**2 + 1 in RR[x,y]) == True

    assert (x**2 + y**2 in EX) == True
    assert (x**2 + y**2 in ZZ) == False
    assert (x**2 + y**2 in QQ) == False
    assert (x**2 + y**2 in RR) == False
    assert (x**2 + y**2 in ALG) == False
    assert (x**2 + y**2 in ZZ[x]) == False
    assert (x**2 + y**2 in QQ[x]) == False
    assert (x**2 + y**2 in RR[x]) == False
    assert (x**2 + y**2 in ZZ[x,y]) == True
    assert (x**2 + y**2 in QQ[x,y]) == True
    assert (x**2 + y**2 in RR[x,y]) == True

def test_PolynomialRing__init():
    raises(GeneratorsNeeded, "ZZ.poly_ring()")

def test_FractionField__init():
    raises(GeneratorsNeeded, "ZZ.frac_field()")

