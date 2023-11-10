from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Video, Categoria, Plataforma


def index(request):
	categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
	videos = get_list_or_404(Video.objects.order_by('nombre'))
	context = {'lista_categorias': categorias, 'lista_videos' : videos  }
	return render(request, 'index.html', context)

#devuelve el listado de videos
def index_videos(request):
	videos = get_list_or_404(Video.objects.order_by('nombre'))
	context = {'lista_videos': videos }
	return render(request, 'videos.html', context)

#devuelve los datos de un video
def show_video(request, video_id):
	video = get_object_or_404(Video, pk=video_id)
	context = {'video': video }
	#output = f'Detalles del video: {video.id}, {video.nombre}, {video.creador}, {video.descripcion}, {video.fecha}. Categorias: {[c.nombre for c in video.categoria_set.all()]}. Plataformas: {[p.nombre for p in video.plataforma_set.all()]}'
	return render(request, 'video.html', context)

#devuelve las categorias de un video
# def index_categorias(request, video_id):
# 	video = Video.objects.get(pk=video_id)
# 	output = ', '.join([c.nombre for c in video.categoria_set.all()])
# 	return HttpResponse(output)

#devuelve las plataformas de un video
# def index_plataformas(request, video_id):
# 	video = get_object_or_404(Video, pk=video_id)
# 	plataformas =  video.plataforma_set.all()
# 	context = {'video': video, 'plataformas' : plataformas }
# 	#output = ', '.join([p.nombre for p in video.plataforma_set.all()])
# 	return render(request, 'plataformas.html', context)

#devuelve el listado de plataformas
def index_plataformas(request):
	plataformas = get_list_or_404(Plataforma.objects.order_by('nombre'))
	context = {'lista_plataformas': plataformas }
	#output = ', '.join([p.nombre for p in video.plataforma_set.all()])
	return render(request, 'plataformas.html', context)  

#devuelve los detalles de una plataforma
def show_plataforma(request, plataforma_id):
	plataforma = get_object_or_404(Plataforma, pk=plataforma_id)
	videos =  plataforma.videos.all()
	context = { 'plataforma': plataforma, 'videos' : videos }
	#output = f'Detalles de la plataforma: {plataforma.id}, {plataforma.nombre}, {plataforma.link}. Videos: {[v.nombre for v in plataforma.video_set.all()]}'
	return render(request, 'plataforma.html', context)

#devuelve el listado de categorias
def index_categorias(request):
	categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
	context = {'lista_categorias': categorias }
	#output = ', '.join([p.nombre for p in video.plataforma_set.all()])
	return render(request, 'categorias.html', context)  

#devuelve los detalles de una categoria
def show_categoria(request, categoria_id):
	categoria = get_object_or_404(Categoria, pk=categoria_id)
	videos =  categoria.videos.all()
	context = { 'categoria': categoria, 'videos' : videos }
	#output = f'Detalles de la categoria: {categoria.id}, {categoria.nombre}, {categoria.descripcion}. Videos: {[v.nombre for v in categoria.video_set.all()]}'
	return render(request, 'categoria.html', context)




