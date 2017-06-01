script = "
# Define a method to print array data
def printArrayData(indent, v):
    count = len(v)
    print '%s#(' % indent,
    for i in xrange(count):
        if i != (count-1):
            print '%s, ' % str(v[i]),
        else:
            print '%s' % str(v[i]),
    print ')'

# Create a standard material
obj = MaxPlus.Factory.CreateMaterial(MaxPlus.ClassIds.Standardmaterial)

# Enumerate across Parameters and print out the properties of each Parameter 
for p in obj.ParameterBlock.Parameters:  
    print ' ', p.Name, p.Type, p.IsObsolete, p.IsAnimatable, p.IsReadOnly, p.IsArrayData, p.Value

# If IsArrayData is true, then print out the array data
    if p.IsArrayData:  
        v = p.Value
        printArrayData(' ', v)

# If IsArrayParameter is true, then cast the Parameter to an ArrayParameter
    if p.IsArrayParameter:  
        pa = MaxPlus.ArrayParameter._CastFrom(p)
        #print out the properties of the ArrayParameter
        print ' ', pa.Name, pa.Type, pa.IsObsolete, pa.IsAnimatable, pa.IsReadOnly, pa.IsArrayData, pa.NumItems, pa.IsResizable, pa.Value  

# For each Parameter in each ArrayParameter, print out its properties
        for v in pa:    
            print ' ', v.TabIndex, v.Name, v.Type, v.IsObsolete, v.IsAnimatable, v.IsReadOnly, v.IsArrayData, v.Value
"

python.execute script