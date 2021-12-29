from manim import *
	
class TangentsComunes(Scene):
    def construct(self):
        ax = NumberPlane(
            x_range=[-4.33,7.15,1],
            y_range=[-3, 7, 1],
            tips=False,
            axis_config={"include_numbers": True},
        ).add_coordinates()

        scale=(ax.c2p(1,0)-ax.c2p(0,0))[0]

        c1=Circle(color=BLUE, radius=1.61*scale).move_to(ax.c2p(-1.72,4.34))
        c1.set_fill(BLUE, opacity=0.5) 
        c2=Circle(color=RED, radius=0.33*scale).move_to(ax.c2p(1.12,2.38))
        c2.set_fill(RED, opacity=0.5) 
        c3=Circle(color=YELLOW, radius=0.63*scale).move_to(ax.c2p(-2.38,1.14)) 
        c3.set_fill(YELLOW, opacity=0.5) 
        self.add(c1,c2,c3)

        l11=Line(ax.c2p(-4.33,-0.43),ax.c2p(7.15,4.73), color=ORANGE)
        l12=Line(ax.c2p(-4.33,1.28),ax.c2p(7.16,4.32), color=ORANGE)
        l21=Line(ax.c2p(-3.97,-3.02),ax.c2p(1.26,6.38), color=GREEN)
        l22=Line(ax.c2p(-2.6,-2.94),ax.c2p(-3.54,6.3), color=GREEN)
        l31=Line(ax.c2p(-1.1,6.32),ax.c2p(5.06,-2.96), color=PURPLE)
        l32=Line(ax.c2p(-4.34,3.27),ax.c2p(7.14,0.68), color=PURPLE)
        self.add(l11,l12,l21,l22,l31,l32)

        p1=Dot(ax.c2p(4.89,3.72), color=ORANGE)
        p2=Dot(ax.c2p(-2.81,-0.93), color=GREEN)
        p3=Dot(ax.c2p(1.85,1.88), color=PURPLE)
        self.add(p1,p2,p3)

        r=Line(ax.c2p(-4.32,-1.84),ax.c2p(7.14,5.07))
        self.add(r)

def circle3D(ax,center=[0,0,0],radius=1):
    surface = Surface(
        lambda u, v: ax.c2p(center[0]+ np.cos(u) * v, center[1]+np.sin(u) * v, center[2]+0),
            u_range=[-PI, PI],
            v_range=[0, radius]
        )
    return surface

def cone3D(ax,apex=[0,0,0],base_center=[0,0,1],radius=1):
    apex=np.array(apex)
    base_center=np.array(base_center)
    director=apex-base_center
    if director[0]==0:
        e1=np.array([1,0,0])
    else:
        e1=np.array([-director[1],director[0],0])/np.linalg.norm(np.array([-director[1],director[0],0]))
    e2=[director[1]*e1[2]-director[2]*e1[1],director[2]*e1[0]-director[0]*e1[2],director[0]*e1[1]-director[1]*e1[0] ]
    e2=e2/np.linalg.norm(e2)

    def func(u,v):
        return base_center + e1* np.cos(u) * v + e2*np.sin(u)*v +director *(1-(v/radius))

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
            u_range=[-PI, PI],
            v_range=[0, 1.5*radius]
        )
    return surface

def sphere3D(ax,center=[0,0,0],radius=1):
    center=np.array(center)

    def func(u,v):
        return center + np.array([np.cos(u) * np.cos(v), np.sin(u)*np.cos(v), np.sin(v)])*radius

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
            u_range=[-PI, PI],
            v_range=[-PI/2, PI/2]
        )
    return surface

def plane3D(ax,p1=[0,0,0],p2=[1,0,0],p3=[0,1,0], x_range=[-10,10], y_range=[-10,10]):
    p1=np.array(p1)
    p2=np.array(p2)
    p3=np.array(p3)

    def func(u,v):
        return p1 + (p2-p1)*u + (p3-p1)*v

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
            u_range=x_range,
            v_range=y_range
        )
    return surface

def lineLong(ax,p1,p2,color=WHITE):
    p1=np.array(p1)
    p2=np.array(p2)
    eps=0.02 #tube's width

    director=p1-p2
    if director[0]==0:
        e1=np.array([1,0,0])
    else:
        e1=np.array([-director[1],director[0],0])/np.linalg.norm(np.array([-director[1],director[0],0]))
    e2=[director[1]*e1[2]-director[2]*e1[1],director[2]*e1[0]-director[0]*e1[2],director[0]*e1[1]-director[1]*e1[0] ]
    e2=e2/np.linalg.norm(e2)


    def func(u):
        return p1 + (p2-p1)*u + e1* np.cos(u) * eps + e2*np.sin(u)*eps 

    linia = Surface(
        lambda u,v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
            u_range=[-1,2],
            v_range=[-PI,PI],
            color=color
    ).set_fill(color, opacity=0.25) 
    return linia


class TangentsComunes3D(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=(-4.33,7.15,1),
            y_range=(-3, 7, 1),
            z_range=(-3, 3, 1),
            tips=False,
            axis_config={"include_numbers": False},
        ).add_coordinates()

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(ax)

        scale=(ax.c2p(1,0)-ax.c2p(0,0))[0]
        c1=circle3D(ax,radius=1.61*scale,center=[-1.72,4.34,0])
        c1.set_fill(BLUE, opacity=0.5) 
        c2=circle3D(ax,radius=0.33*scale,center=[1.12,2.38,0])
        c2.set_fill(RED, opacity=0.5) 
        c3=circle3D(ax,radius=0.63*scale,center=[-2.38,1.14,0])
        c3.set_fill(YELLOW, opacity=0.5) 
        self.add(c1,c2,c3)

        l11=Line3D(ax.c2p(-4.33,-0.43),ax.c2p(7.15,4.73,0), color=ORANGE)
        l12=Line3D(ax.c2p(-4.33,1.28),ax.c2p(7.16,4.32,0), color=ORANGE)
        l21=Line3D(ax.c2p(-3.97,-3.02),ax.c2p(1.26,6.38,0), color=GREEN)
        l22=Line3D(ax.c2p(-2.6,-2.94),ax.c2p(-3.54,6.3,0), color=GREEN)
        l31=Line3D(ax.c2p(-1.1,6.32),ax.c2p(5.06,-2.96,0), color=PURPLE)
        l32=Line3D(ax.c2p(-4.34,3.27),ax.c2p(7.14,0.68,0), color=PURPLE)
        self.add(l11,l12,l21,l22,l31,l32)

        p1=Dot3D(ax.c2p(4.89,3.72,0), color=ORANGE)
        p2=Dot3D(ax.c2p(-2.81,-0.93,0), color=GREEN)
        p3=Dot3D(ax.c2p(1.85,1.88,0), color=PURPLE)
        self.add(p1,p2,p3)

        r=Line3D(ax.c2p(-4.32,-1.84,0),ax.c2p(7.14,5.07,0))
        self.add(r)

        s1=sphere3D(ax, center=[-1.72,4.34,0],radius=1.61)
        s1.set_color(BLUE)
        s2=sphere3D(ax, center=[1.12,2.38,0], radius=0.33)
        s2.set_color(RED)
        s3=sphere3D(ax, center=[-2.38,1.14,0], radius=0.63) 
        s3.set_color(YELLOW)
        self.add(s1,s2,s3)

        con1=cone3D(ax,apex=[4.89,3.72,0],base_center=[-2.33,1.16,0],radius=0.63)
        con1.set_fill(ORANGE, opacity=0.5)
        con2=cone3D(ax,apex=[-2.81,-0.93,0],base_center=[-1.82,3.87,0],radius=1.54)
        con2.set_fill(GREEN, opacity=0.5)
        con3=cone3D(ax,apex=[1.85,1.88,0],base_center=[-1.23,4,0],radius=1.5)
        con3.set_fill(BLUE, opacity=0.5)
        
        q1=Dot3D(ax.c2p(-2.33,1.16,0.63),color=ORANGE)
        q1p=Dot3D(ax.c2p(1.15,2.39,0.33),color=ORANGE)
        q2=Dot3D(ax.c2p(-1.82,3.87,1.54),color=GREEN)
        q2p=Dot3D(ax.c2p(-2.42,0.95,0.6),color=ORANGE)
        q3=Dot3D(ax.c2p(-1.23,4,1.5),color=PURPLE)
        q3p=Dot3D(ax.c2p(1.22,2.31,0.3),color=ORANGE)
        l13= lineLong(ax,q1.get_center(),p1.get_center(), color=ORANGE)
        l23= lineLong(ax,q2.get_center(),p2.get_center(), color=GREEN)
        l33= lineLong(ax,q3.get_center(),p3.get_center(), color=PURPLE)
        self.add(con1,con2,con3,q1,q2,q3,q1p,q2p,q3p,l13,l23,l33)

        plah= plane3D(ax,x_range=[-7,7],y_range=[-3,7])
        plah.set_fill(WHITE, opacity=0.25)
        platan= plane3D(ax,p1.get_center(),p2.get_center(),q1.get_center(),x_range=[-2,2],y_range=[-2,2])
        platan.set_fill(WHITE, opacity=0.25)
#        self.add(plah,platan)

#        self.begin_ambient_camera_rotation(rate=0.1)
#        self.wait()
#        self.stop_ambient_camera_rotation()
#        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
#        self.wait()


class CantorSet(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-0.5,1.5,1],
            y_range=[-0.2, 1.2, 1],
            tips=False,
            axis_config={"include_numbers": True},
        ).add_coordinates()

#        p=(1,0)
#        q=(1,1)
#        l=[Line(ax.c2p(p[0],p[1]),ax.c2p(q[0],q[1]))]
        m=5
        p_ini=[[(0,1)]]
        p_fin=[[(1,1)]]
        l=[[Line(ax.c2p(p_ini[0][0][0],p_ini[0][0][1]),ax.c2p(p_fin[0][0][0],p_fin[0][0][1]))]]
        for k in range(m):
            p_ini.append([])
            p_fin.append([])
            l.append([])
            for j in range( len(p_ini[k])):
                p_ini[k+1].append(p_ini[k][j] + (0,-1./m))
                p_fin[k+1].append(p_ini[k][j] + (1./3**(k+2),-1./m))
                p_ini[k+1].append(p_ini[k][j] + (2./3**(k+2),-1./m))
                p_fin[k+1].append(p_ini[k][j] + (1./3**(k+1),-1./m))
                l[k+1].append(Line(ax.c2p(p_ini[k+1][2*j][0],p_ini[k+1][2*j][1]),ax.c2p(p_fin[k+1][2*j][0],p_fin[k+1][2*j][1])))
                l[k+1].append(Line(ax.c2p(p_ini[k+1][2*j+1][0],p_ini[k+1][2*j+1][1]),ax.c2p(p_fin[k+1][2*j+1][0],p_fin[k+1][2*j+1][1])))
        for k in l:
            for j in k:
             self.play(Create(j))
        self.wait()
