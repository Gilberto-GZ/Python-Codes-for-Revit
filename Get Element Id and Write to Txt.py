tag_list = FilteredElementCollector(doc).OfClass(IndependentTag).WhereElementIsNotElementType().ToElements()
#cb_tags = []


tag_list = FilteredElementCollector(doc).OfClass(IndependentTag).WhereElementIsNotElementType().ToElements()

for tag in tag_list:
    tag_text = tag.TagText

    
    
    if "CB-" in tag_text:
        tag_id = tag.Id.ToString()
        f= open("C:\Users\ggzapatero\Documents\Tags.txt","a+")

        f.write(tag_id + ",")

        f.close()
		
		
