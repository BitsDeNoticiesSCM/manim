from manim import *
# import numpy as np

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
        cercles=VGroup(c1,c2,c3)

        l11=Line(ax.c2p(-4.33,-0.43),ax.c2p(7.15,4.73), color=ORANGE)
        l12=Line(ax.c2p(-4.33,1.28),ax.c2p(7.16,4.32), color=ORANGE)
        l21=Line(ax.c2p(-3.97,-3.02),ax.c2p(1.26,6.38), color=GREEN)
        l22=Line(ax.c2p(-2.6,-2.94),ax.c2p(-3.54,6.3), color=GREEN)
        l31=Line(ax.c2p(-1.1,6.32),ax.c2p(5.06,-2.96), color=PURPLE)
        l32=Line(ax.c2p(-4.34,3.27),ax.c2p(7.14,0.68), color=PURPLE)
        tangentsComunes=VGroup(l11,l12,l21,l22,l31,l32)

        p1=Dot(ax.c2p(4.89,3.72), color=ORANGE)
        p2=Dot(ax.c2p(-2.81,-0.93), color=GREEN)
        p3=Dot(ax.c2p(1.85,1.88), color=PURPLE)
        interseccions=VGroup(p1,p2,p3)

        r=Line(ax.c2p(-4.32,-1.84),ax.c2p(7.14,5.07))

        self.wait(10)

        monge = ImageMobject("Monge.jpg")
        monge.scale(1.2)
        monge.to_edge(RIGHT, buff=1)
        self.add(monge)
        self.wait(10)
        self.remove(monge)
        self.wait(5)

        self.play(Create(cercles), run_time=3)
        self.wait(2)
        self.play(Create(tangentsComunes), run_time=3)
        self.wait(2)
        self.play(Create(interseccions))
        self.wait(7)
        self.play(Create(r))
        self.wait(21)
        self.play(
            FadeOut(cercles),
            FadeOut(tangentsComunes),
            FadeOut(interseccions),
            FadeOut(r)
        )
        self.wait(2)
    def construccioQuieta(self):
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
        cercles=VGroup(c1,c2,c3)

        l11=Line(ax.c2p(-4.33,-0.43),ax.c2p(7.15,4.73), color=ORANGE)
        l12=Line(ax.c2p(-4.33,1.28),ax.c2p(7.16,4.32), color=ORANGE)
        l21=Line(ax.c2p(-3.97,-3.02),ax.c2p(1.26,6.38), color=GREEN)
        l22=Line(ax.c2p(-2.6,-2.94),ax.c2p(-3.54,6.3), color=GREEN)
        l31=Line(ax.c2p(-1.1,6.32),ax.c2p(5.06,-2.96), color=PURPLE)
        l32=Line(ax.c2p(-4.34,3.27),ax.c2p(7.14,0.68), color=PURPLE)
        tangentsComunes=VGroup(l11,l12,l21,l22,l31,l32)

        p1=Dot(ax.c2p(4.89,3.72), color=ORANGE)
        p2=Dot(ax.c2p(-2.81,-0.93), color=GREEN)
        p3=Dot(ax.c2p(1.85,1.88), color=PURPLE)
        interseccions=VGroup(p1,p2,p3)

        r=Line(ax.c2p(-4.32,-1.84),ax.c2p(7.14,5.07))

        self.play(
            Create(cercles),
            Create(tangentsComunes), 
            Create(interseccions),
            Create(r),
            run_time=3
        )
        self.wait(20)
        self.play(
            FadeOut(cercles),
            FadeOut(tangentsComunes),
            FadeOut(interseccions),
            FadeOut(r)
        )
        self.wait(2)

def circle3D(ax,center=[0,0,0],radius=1,color=WHITE):
    surface = Surface(
        lambda u, v: ax.c2p(center[0]+ np.cos(u) * v, center[1]+np.sin(u) * v, center[2]+0),
        u_range=[-PI, PI],
        v_range=[0, radius],
        stroke_width=0
    ).set_fill(color)
    return surface

def cone3D(ax,apex=[0,0,0],base_center=[0,0,1],radius=1,color=WHITE):
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
        return base_center + e2* np.cos(u) * v + e1*np.sin(u)*v +director *(1-(v/radius))

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
        u_range=[-PI, PI],
        v_range=[-0.5*radius, 1.5*radius]
    ).set_fill(color)
    return surface

def sphere3D(ax,center=[0,0,0],radius=1,color=WHITE):
    center=np.array(center)

    def func(u,v):
        return center + np.array([np.cos(u) * np.cos(v), np.sin(u)*np.cos(v), np.sin(v)])*radius

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
        u_range=[-PI, PI],
        v_range=[-PI/2, PI/2]
    ).set_fill(color)
    return surface

def plane3D(ax,p1=[0,0,0],p2=[1,0,0],p3=[0,1,0], x_range=[-10,10], y_range=[-10,10],color=WHITE):
    p1=np.array(p1)
    p2=np.array(p2)
    p3=np.array(p3)

    e0=(p2-p1)/np.linalg.norm(p2-p1)
    e1=np.cross(p2-p1,p3-p1)
    e2=np.cross(e1,e0)
    e2=e2/np.linalg.norm(e2)


    def func(u,v):
        return p1 + e0*u + e2*v

    surface = Surface(
        lambda u, v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
        u_range=x_range,
        v_range=y_range
    ).set_fill(color, opacity=0.25)
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


    def func(u,v):
        return p1 + (p2-p1)*u + e1* np.cos(v) * eps + e2*np.sin(v)*eps 

    linia = Surface(
        lambda u,v: ax.c2p(func(u,v)[0],func(u,v)[1],func(u,v)[2]),
        u_range=[-1,2],
        v_range=[-PI,PI],
        stroke_width=0
    ).set_fill(color)
    return linia


class TangentsComunes3D(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            x_range=(-4.33,7.15,1),
            y_range=(-3, 7, 1),
            z_range=(-3, 3, 1),
            tips=False,
            axis_config={"include_numbers": False},
        )

#Definició de les esferes
        s1=sphere3D(ax, center=[-1.72,4.34,0],radius=1.61)
        s1.set_color(BLUE)
        s2=sphere3D(ax, center=[1.12,2.38,0], radius=0.33)
        s2.set_color(RED)
        s3=sphere3D(ax, center=[-2.38,1.14,0], radius=0.63) 
        s3.set_color(YELLOW)
        esferes=VGroup(s1,s2,s3)

#Aparició de les esferes
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=-0.1)
        self.play(GrowFromCenter(esferes), run_time=3)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=85 * DEGREES, theta=30 * DEGREES)

#Plans tangents
        platan= plane3D(ax, [4.89,3.72,0], [-2.81,-0.93,0],[-1.38,3.78,1.47],x_range=[0,10],y_range=[-3,7])
        platan2= plane3D(ax, [4.89,3.72,0], [-2.81,-0.93,0],[-1.38,3.78,-1.47],x_range=[0,10],y_range=[-3,7])
        plansTangents=VGroup(platan,platan2)
        self.play(Create(plansTangents), run_time=3)
        self.wait(2)

#Punts de tangència de les esferes amb els plans
        q1=Dot3D(ax.c2p(-1.38,3.78,1.47),color=BLUE)
        q2=Dot3D(ax.c2p(1.19,2.27,0.3),color=RED)
        q3=Dot3D(ax.c2p(-2.25,0.92,0.58),color=YELLOW)
        q1d=Dot3D(ax.c2p(-1.38,3.78,-1.47),color=BLUE)
        q2d=Dot3D(ax.c2p(1.19,2.27,-0.3),color=RED)
        q3d=Dot3D(ax.c2p(-2.25,0.92,-0.58),color=YELLOW)
        puntsEsferes=VGroup(q1,q2,q3,q1d,q2d,q3d)
        puntsEsferes=VGroup(q1,q2,q3,q1d,q2d,q3d)
        self.play(Create(puntsEsferes), run_time=7)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

#Recta de Monge
        r=Line3D(ax.c2p(-4.32,-1.84,0),ax.c2p(7.14,5.07,0))
        self.play(Create(r))
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.wait(2)

#Rectes tangents a dues esferes dels plans tangents
        l13= lineLong(ax,[-2.25,0.92,0.58],[4.89,3.72,0], color=ORANGE)
        l23= lineLong(ax,[-1.38,3.78,1.47],[-2.81,-0.93,0], color=GREEN)
        l33= lineLong(ax,[-1.38,3.78,1.47],[1.85,1.88,0], color=PURPLE)
        ld13= lineLong(ax,[-2.25,0.92,-0.58],[4.89,3.72,0], color=ORANGE)
        ld23= lineLong(ax,[-1.38,3.78,-1.47],[-2.81,-0.93,0], color=GREEN)
        ld33= lineLong(ax,[-1.38,3.78,-1.47],[1.85,1.88,0], color=PURPLE)
        rectesPlansG=VGroup(l23,ld23)
        rectesPlansOP=VGroup(l13,l33,ld13,ld33)    

#Vèrtexs dels cons, (o intersecció de les tangents)
        p1=Dot3D(ax.c2p(4.89,3.72,0), color=ORANGE)
        p2=Dot3D(ax.c2p(-2.81,-0.93,0), color=GREEN)
        p3=Dot3D(ax.c2p(1.85,1.88,0), color=PURPLE)
        InterseccionsOP=VGroup(p1,p3)


        self.play(Create(rectesPlansG), run_time=3)
        self.wait(18)
        self.play(Create(p2), run_time=1)

        self.play(Create(rectesPlansOP), run_time=3)
        self.wait(19)
        self.play(Create(InterseccionsOP), run_time=1)

        self.play(FadeOut(plansTangents))
        self.wait(5)

#Cons tangents a dues esferes
        con1=cone3D(ax,apex=[4.89,3.72,0],base_center=[-2.33,1.16,0],radius=0.63)
        con1.set_fill(ORANGE, opacity=0.5)
        con2=cone3D(ax,apex=[-2.81,-0.93,0],base_center=[-1.82,3.87,0],radius=1.54)
        con2.set_fill(GREEN, opacity=0.5)
        con3=cone3D(ax,apex=[1.85,1.88,0],base_center=[-1.23,4,0],radius=1.5)
        con3.set_fill(BLUE, opacity=0.5)
        consOP=VGroup(con1,con3)
        self.play(Create(con2),FadeOut(rectesPlansG), run_time=3)
        self.wait(6)        
        self.play(Create(consOP),FadeOut(rectesPlansOP), run_time=3)
        self.wait(3)        

#Pla horitzontal i eixos
        plah= plane3D(ax,x_range=[-7,7],y_range=[-3,7])
        self.play(Create(plah),Create(ax), run_time=1)
        self.wait(7)

#Tangents comunes a les circumferències
        l11=Line3D(ax.c2p(-4.33,-0.43),ax.c2p(7.15,4.73,0), color=ORANGE)
        l12=Line3D(ax.c2p(-4.33,1.28),ax.c2p(7.16,4.32,0), color=ORANGE)
        l21=Line3D(ax.c2p(-3.97,-3.02),ax.c2p(1.26,6.38,0), color=GREEN)
        l22=Line3D(ax.c2p(-2.6,-2.94),ax.c2p(-3.54,6.3,0), color=GREEN)
        l31=Line3D(ax.c2p(-1.1,6.32),ax.c2p(5.06,-2.96,0), color=PURPLE)
        l32=Line3D(ax.c2p(-4.34,3.27),ax.c2p(7.14,0.68,0), color=PURPLE)
        tangentsComunes=VGroup(l11,l12,l21,l22,l31,l32)

#Circumferències
        c1=circle3D(ax,radius=1.61,center=[-1.72,4.34,0])
        c1.set_fill(BLUE, opacity=1) 
        c2=circle3D(ax,radius=0.33,center=[1.12,2.38,0])
        c2.set_fill(RED, opacity=1) 
        c3=circle3D(ax,radius=0.63,center=[-2.38,1.14,0])
        c3.set_fill(YELLOW, opacity=1)
        cercles=VGroup(c1,c2,c3) 
        self.play(Create(cercles), run_time=3)
        self.play(FadeOut(esferes),FadeOut(puntsEsferes), run_time=3)
        self.play(Create(tangentsComunes), run_time=3)
        self.play(FadeOut(con2),FadeOut(consOP), run_time=3)
        self.wait(7)

        self.move_camera(phi=0 * DEGREES, theta=270 * DEGREES, run_time=5)
        self.wait(14)
        self.play(
            FadeOut(ax),
            FadeOut(plah),
            FadeOut(tangentsComunes),
            FadeOut(cercles),
            FadeOut(InterseccionsOP),
            FadeOut(p2),
            FadeOut(r)
        )


        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

#Resum
        self.play(
            Create(plah),
            Create(cercles),
            Create(tangentsComunes)
        )
        self.play(
            Create(ax),
            Create(esferes),
            Create(con2),
            Create(consOP),
            Create(InterseccionsOP),
            Create(p2)
        )
        self.play(
            Create(puntsEsferes),
            Create(rectesPlansG),
            Create(rectesPlansOP)
        )
        self.play(
            Create(plansTangents)
        )
        self.play(
            Create(r)
        )
        
        self.wait(30)

        self.play(
            FadeOut(plah),
            FadeOut(cercles),
            FadeOut(tangentsComunes),
            FadeOut(ax),
            FadeOut(esferes),
            FadeOut(con2),
            FadeOut(consOP),
            FadeOut(InterseccionsOP),
            FadeOut(p2),
            FadeOut(puntsEsferes),
            FadeOut(rectesPlansG),
            FadeOut(rectesPlansOP),
            FadeOut(plansTangents),
            FadeOut(r),
        )
        self.move_camera(phi=0 * DEGREES, theta=270 * DEGREES, run_time=5)

class Conclusions(Scene):
    def construct(self): 
        cubica = MathTex(r"a{{x}}^3+b{{x}}^2+c{{x}}+d=0", font_size=30)
        discriminants = MathTex(r"{{\Delta_0}}=b^2-3ac\quad {{\Delta_1}}= 2b^3-9abc+27a^2d", font_size=30)
        C = MathTex(r"C=\sqrt[3]{\frac{\Delta_1 \pm \sqrt{\Delta_1^2-4\Delta_0^3}}{2}}", font_size=30)
        sol = MathTex(r"x=-\frac{1}{3a}\left(b+\xi^kC+\frac{\Delta_0}{\xi^k C}\right)\quad k\in\{0,1,2\}", font_size=30)
        unitat = MathTex(r"\xi=\frac{-1}{2} + \frac{\sqrt{3}}2 {{i}}", font_size=45)
        unitat.submobjects[1].set_color(YELLOW)
        
        discriminants.next_to(cubica, DOWN)
        C.next_to(discriminants, DOWN)
        sol.next_to(C, DOWN)
        unitat.next_to(sol, DOWN)
        complexosTot=VGroup(cubica,discriminants,C,sol,unitat).move_to(ORIGIN).to_edge(LEFT)

        self.wait(5)
        self.play(Create(cubica))
        self.play(Create(discriminants))
        self.play(TransformMatchingTex(discriminants.copy(), C))
        self.play(Create(sol))
        self.play(Create(unitat))
        self.wait(2)

        laplacia = MathTex(r"{{(-\Delta)^{\frac12} f(x)=}} c \int_{\mathbb{R}^d} \frac{f(x)-f(y)}{|x-y|^{d+1}}\, dy", font_size=40)
        dirichletToNeumann = MathTex(r"{{(-\Delta)^{\frac12} f(x)=}} c \lim_{y\to 0} \frac{u(x,y)-u(x,0)}{|y|}", font_size=40)
        extensio = MathTex(r"\begin{cases}\Delta u =0\\ u(x,0)=f(x)\end{cases}", font_size=40)
        extensio.next_to(laplacia, DOWN)
        dirichletToNeumann.next_to(extensio, DOWN)
        laplaciaTot=VGroup(laplacia,dirichletToNeumann,extensio).move_to(ORIGIN).to_edge(RIGHT)

        self.play(Create(laplacia))
        self.wait(3)
        self.play(Create(extensio))
        self.play(TransformMatchingTex(laplacia.copy(),dirichletToNeumann))
        self.wait(4)
        
        self.play(
            FadeOut(complexosTot),
            FadeOut(laplaciaTot)
        )
        self.wait(3)

class LogoFinal(Scene):
    def construct(self):
        noticies = ImageMobject("logo.png")
        noticies.scale(1.2)
        self.add(noticies)
        self.wait(32)

class CantorSet(Scene): #Classe per crear una escena
    def construct(self): 
#Inicialitzem eixos de coordenades i variables
        ax = Axes(x_range=[-0.5,1.5], y_range=[-0.2, 1.2])
        m=7; lpre=[]; lpost=[]
        for j in range(m+1): lpre.append([]); lpost.append([])
#Iteració del conjunt de Cantor
        def cantorize(p1,p2,o):
            lpre[o].append(Line(ax.c2p(p1[0],p1[1]+1./m),ax.c2p(p2[0],p2[1]+1./m),color=GREEN))
            lpost[o].append(Line(ax.c2p(p1[0],p1[1]),ax.c2p(p2[0],p2[1]),color=RED))
            if o<m: #Iteracions:
                cantorize(p1 + (0,-1./m),p1+(p2-p1)/3.+(0,-1./m),o+1)
                cantorize(p1+(p2-p1)*2/3.+(0,-1./m),p2+(0,-1./m),o+1)
        cantorize(np.array([0,1]),np.array([1,1]),0)
#Creació de l'animació: apareixen successivament les línies grogues (lpre) i es converteixen en les taronges (lpost) creant efecte de ``pluja de Cantor''
        for k in range(len(lpost)):
            mpre=VGroup(*lpre[k])
            mpost=VGroup(*lpost[k])
            self.play(FadeIn(mpre))
            self.play(ReplacementTransform(mpre,mpost))
            self.wait()

class AnimatedCircleToTex(Scene):
    def construct(self): #Constructor
        # Definició dels objectes
        circle = Circle().set_fill(PINK, opacity=0.5)
        text = MathTex(r"x^{{2}}+{{y^2}}={{1}}", font_size=96, color=BLACK)
        text.submobjects[1].set_color(PURE_RED)
        text2 = MathTex(r"x{{=}}{{\sqrt}}{1{{-}}y^2}", font_size=96, color=BLACK)
        text2.set_color_by_tex("\sqrt", PURE_RED)
        # Emplacement dels objectes
        text2.next_to(text, DOWN)
        VGroup(text,text2).next_to(circle, RIGHT)
        VGroup(circle,text,text2).move_to(ORIGIN)
        # Creació de l'animació
        self.play(Create(circle))
        self.play(ReplacementTransform(circle.copy(), text))
        self.play(TransformMatchingTex(text.copy(), text2, transform_mismatches=True,key_map={"1":"1", "+":"-", "2": "\sqrt"}))
        self.wait()

class DosEixos(Scene):
    def construct(self):
        eix1 = Axes(x_range=[-2,4], y_range=[0,10], x_length=5).set_color(BLACK) 
        eix2 = eix1.copy()
        eix1.to_edge(LEFT)
        eix2.to_edge(RIGHT)
        eixos= VGroup(eix1,eix2)
        #Funció a dibuixar
        def func(x):
            return abs(np.log(abs(x))+x**2-1)
        corba1 = eix1.plot(func, color=PURE_RED)
        corba2 = eix2.plot(func, x_range=(-1.9999, 4, 0.002), color=ORANGE)
        corbes = VGroup(corba1,corba2)
        self.add(eixos,corbes)

class TeoremaDeMonge1(Scene):
    def construct(self):
        TangentsComunes.construct(self)
class TeoremaDeMonge2(ThreeDScene):
    def construct(self):
        TangentsComunes3D.construct(self)
class TeoremaDeMonge3(Scene):
    def construct(self):
        Conclusions.construct(self)
        TangentsComunes.construccioQuieta(self)
        LogoFinal.construct(self)


