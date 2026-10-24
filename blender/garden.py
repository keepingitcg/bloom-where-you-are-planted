import bpy, math, random, os
from mathutils import Vector
random.seed(9)
out=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
def mat(n,c):
 m=bpy.data.materials.new(n); m.diffuse_color=(*c,1); m.use_nodes=True; m.node_tree.nodes.get('Principled BSDF').inputs['Base Color'].default_value=(*c,1); return m
 grass=0
moss=mat('Matcha meadow',(.36,.55,.26)); soil=mat('Warm earth',(.29,.20,.14)); bark=mat('Cedar',(.35,.23,.16)); leaf=mat('Jade',(.26,.49,.29)); lightleaf=mat('Sunlit sage',(.52,.66,.33)); stone=mat('River stone',(.61,.65,.56))
def sphere(n,loc,scale,m,sub=2):
 bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=sub,radius=1,location=loc); o=bpy.context.object;o.name=n;o.scale=scale;o.data.materials.append(m);return o
def branch(a,b,r,m):
 d=Vector(b)-Vector(a);bpy.ops.mesh.primitive_cone_add(vertices=9,radius1=r,radius2=r*.65,depth=d.length,location=(Vector(a)+Vector(b))/2);o=bpy.context.object;o.rotation_euler=d.to_track_quat('Z','Y').to_euler();o.data.materials.append(m)
sphere('Floating earth',(0,0,-.42),(3.5,2.65,.8),soil)
sphere('Soft meadow',(0,0,-.05),(3.55,2.7,.38),moss)
for i in range(28):
 x=random.uniform(-3,3);y=random.uniform(-2,2)
 if x*x/10+y*y/5<1:sphere('Meadow pebble',(x,y,.2),(random.uniform(.08,.22),.13,.1),stone,1)
base=set(bpy.data.objects)
def tree(x,y,s):
 branch((x,y,.1),(x,y,2.7*s),.16*s,bark)
 for z,dx,dy in [(1.3,-.65,.1),(1.8,.7,.05),(2.1,-.25,-.4)]:branch((x,y,z*s),(x+dx*s,y+dy*s,(z+.6)*s),.08*s,bark)
 for dx,dy,z,r in [(0,0,2.9,.88),(-.65,.1,2.5,.78),(.65,.05,2.6,.85),(-.25,-.45,2.35,.7),(0,.45,2.5,.8)]:sphere('Painted canopy',(x+dx*s,y+dy*s,z*s),(r*s,r*.85*s,r*.8*s),random.choice([leaf,lightleaf]))
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24
scene.render.resolution_x=1100;scene.render.resolution_y=850;scene.render.resolution_percentage=100;scene.render.film_transparent=True
scene.world.color=(.65,.65,.65)
bpy.ops.object.light_add(type='AREA',location=(-3,-4,8));bpy.context.object.data.energy=650;bpy.context.object.data.size=7
bpy.ops.object.camera_add(location=(7,-11,8));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,1))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=10.8;scene.camera=cam
fixed=set(bpy.data.objects)
for stage in range(4):
 for o in list(bpy.data.objects):
  if o not in fixed:bpy.data.objects.remove(o,do_unlink=True)
 if stage==0:sphere('A small beginning',(0,0,.43),(.28,.2,.2),bark)
 elif stage==1:
  branch((0,0,.1),(0,0,.8),.04,leaf)
  sphere('First leaf',(-.2,0,.7),(.32,.12,.13),lightleaf);sphere('Second leaf',(.2,0,.85),(.32,.12,.13),leaf)
 elif stage==2:tree(0,0,1)
 else:
  for x,y,s in [(-1.5,.8,.8),(0,1.1,1),(1.5,.6,.85),(-1.1,-.8,.8),(1,-.8,1.05)]:tree(x,y,s)
 scene.render.filepath=os.path.join(out,'assets',f'stage-{stage}.png');bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out,'blender','garden.blend'))
