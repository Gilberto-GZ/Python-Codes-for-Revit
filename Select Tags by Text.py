
from System.Collections.Generic import List

tag_list = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(IndependentTag).WhereElementIsNotElementType().ToElements()
filtered_tags = []
for tag in tag_list:
	tag_text = tag.TagText
	

	
	
	if "CB" in tag_text:
		print(tag_text)
		filtered_tags.append(tag)
		
		uidoc = __revit__.ActiveUIDocument
		selection = uidoc.Selection
		selection.SetElementIds(List[ElementId]([tag.Id for tag in filtered_tags]))
	
		
