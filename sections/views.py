from django.shortcuts import render,Http404
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'index.html')

text=[" Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maiores, laborum tenetur id, numquam expedita dolor nobis perferendis inventore impedit quasi illo cumque tempora? Quod, commodi? Consequatur illo deserunt soluta sit.", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sed quam neque est nemo molestiae, repudiandae eligendi voluptatem exercitationem ipsa culpa perspiciatis dignissimos, harum ipsam praesentium facere! Deserunt vitae dolorem, quam asperiores doloribus officiis dolorum esse modi earum est explicabo, a tenetur eos rem id veritatis iusto. At et ea fuga perspiciatis sequi voluptatibus temporibus laborum nobis? Voluptates quaerat tempore eaque.","Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur tenetur, minus repellat illum praesentium ad impedit hic vero magnam nobis voluptate est explicabo porro corrupti quam delectus aut blanditiis molestias sit veniam sequi? Minus optio quod, quas eius soluta nesciunt sapiente reiciendis, officiis molestias dolorum temporibus necessitatibus. Vitae numquam unde similique doloribus dolore consequatur quos voluptatem illo laudantium culpa harum, ullam quam deleniti. Laboriosam excepturi, temporibus perspiciatis, dignissimos eum maxime eaque commodi corporis, ut maiores porro tempore eius nesciunt voluptas aliquid sint dolore ex fugiat explicabo magni. Velit, ex illum!"]


def sect(request,num):
    if(num>=1 and num<=3):
        return HttpResponse(text[num-1])         
    else:
        raise Http404("No Such Sections")

def posts(request):
    return render(request,'posts.html')

def postrequest(request):
    start=int(request.GET.get("start"))
    end=int(request.GET.get("end"))

    data=[]
    for i in range(start,end+1):
        data.append(f"Post #{i}")

    return JsonResponse(data,safe=False)

    



    
                                                                            
    