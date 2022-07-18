from django.shortcuts import render
from django.http import JsonResponse
from docx import Document
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import json
import io

# Create your views here.
@csrf_exempt
def format(request):
  
  config = json.loads(request.POST['config'])
  file = request.FILES['file']

  # TODO perform some document edits here
  document = Document(file)

  response = StreamingHttpResponse(
    streaming_content = FileWrapper(file),
    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
  )

  response['Content-Disposition'] = 'attachment;filename=Test.docx'
  response["Content-Encoding"] = 'UTF-8'

  return response