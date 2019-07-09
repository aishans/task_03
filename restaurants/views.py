from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	"my_list" : [
    		#restaurant1:
    		{
    		"Restaurant_name": "Five Guys",
    		"Food_Type": "American cuisine"
    		},
    		#restaurant1:
    		{
    		"Restaurant_name": "Ora",
    		"Food_Type": "japanese "
    		},
    		#restaurant1:
    		{
    		"Restaurant_name": "Burger King",
    		"Food_Type": "fast food"
    		}
    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context =   { 
    	
   
    		"my_object":
    		{
    			"Restaurant_name": "Tatami",
    			"food_Type": "japanese"
    		}


    	}

    
    return render(request, 'detail.html', context)
