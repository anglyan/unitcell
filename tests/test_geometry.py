import unittest as ut
from unitcell.geometry import Vec3, vprod, scalar

class TestBasicOperations(ut.TestCase):

    def setUp(self):
        self.v1 = Vec3(1.0, 1.0, 2.0)
        self.v2 = Vec3(2.0, 0.0, -1.0)

    def assertSameVecs(self, v1, v2):
        self.assertAlmostEqual(v1.x, v2.x)
        self.assertAlmostEqual(v1.y, v2.y)
        self.assertAlmostEqual(v1.z, v2.z)
    
    def test_operations(self):
        self.assertSameVecs(self.v1+self.v2, Vec3(3.0, 1.0, 1.0))
        self.assertSameVecs(-self.v1, Vec3(-1.0, -1.0, -2.0))
        self.assertSameVecs(self.v1/2, Vec3(0.5, 0.5, 1.0))
        self.assertSameVecs(2*self.v1, Vec3(2,2,4))
        self.assertSameVecs(self.v1-self.v2, Vec3(-1,1,3))
        self.assertAlmostEqual(scalar(self.v1, self.v2), 0.0)


class TestVectorProd(ut.TestCase):

    def setUp(self) -> None:
        self.v1 = Vec3(1.0, 0.0, 0.0)
        self.v2 = Vec3(0.0, 1.0, 0.0)
        self.v3 = Vec3(0.0, 0.0, 1.0)
        self.v4 = Vec3(1.0, 2.0, 0.0)
        self.v5 = Vec3(0.0, 1.0, 2.0)
        self.v6 = Vec3(1.0, 0.0, 2.0)
        self.vlist = [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6]

        return super().setUp()
    
    def assertSameVecs(self, v1, v2):
        self.assertAlmostEqual(v1.x, v2.x)
        self.assertAlmostEqual(v1.y, v2.y)
        self.assertAlmostEqual(v1.z, v2.z)

    def test_orthogonal(self):
        vout = vprod(self.v1, self.v2)
        self.assertSameVecs(vout, self.v3)
        vout = vprod(self.v1, self.v3)
        self.assertSameVecs(vout, -self.v2)
        vout = vprod(self.v2, self.v3)
        self.assertSameVecs(vout, self.v1)

    def test_outofplane(self):
        vout = vprod(self.v1, self.v4)
        self.assertSameVecs(vout, Vec3(0.0, 0.0, 2.0))
        vout = vprod(self.v3, self.v5)
        self.assertSameVecs(vout, -Vec3(1.0, 0.0, 0.0))

    def test_parallel(self):
        for v in self.vlist:
            self.assertAlmostEqual(abs(vprod(v,v)), 0.0)


class TestRotate(ut.TestCase):

    def setUp(self) -> None:
        self.v1 = Vec3(1.0, 0.0, 0.0)
        self.v2 = Vec3(0.0, 1.0, 0.0)
        self.v3 = Vec3(0.0, 0.0, 1.0)

        return super().setUp()
    
    def assertSameVecs(self, v1, v2):
        self.assertAlmostEqual(v1.x, v2.x)
        self.assertAlmostEqual(v1.y, v2.y)
        self.assertAlmostEqual(v1.z, v2.z)

    def test_xrotate(self):
        self.assertSameVecs(Vec3(1,0,0).xrotate(90), self.v1)
        self.assertSameVecs(Vec3(0,1,0).xrotate(90), self.v3)
        self.assertSameVecs(Vec3(0,0,1).xrotate(90), -self.v2)
        self.assertSameVecs(Vec3(0,1,0).xrotate(-90), -self.v3)
        self.assertSameVecs(Vec3(0,0,1).xrotate(-90), self.v2)

    def test_yrotate(self):
        self.assertSameVecs(Vec3(0,1,0).yrotate(90), self.v2)
        self.assertSameVecs(Vec3(1,0,0).yrotate(90), -self.v3)
        self.assertSameVecs(Vec3(0,0,1).yrotate(90), self.v1)
        self.assertSameVecs(Vec3(1,0,0).yrotate(-90), self.v3)
        self.assertSameVecs(Vec3(0,0,1).yrotate(-90), -self.v1)


    def test_zrotate(self):
        self.assertSameVecs(Vec3(0,0,1).zrotate(90), self.v3)
        self.assertSameVecs(Vec3(1,0,0).zrotate(90), self.v2)
        self.assertSameVecs(Vec3(0,1,0).zrotate(90), -self.v1)
        self.assertSameVecs(Vec3(1,0,0).zrotate(-90), -self.v2)
        self.assertSameVecs(Vec3(0,1,0).zrotate(-90), self.v1)
