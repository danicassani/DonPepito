year = 1995
filename = "year.txt"
path = "C:"

pipeline
{
    agent any
    stages
    {
        stage("FIRST STAGE")
        {
            steps
            {
                script
                {
                    fecha = new Date()
                    current_year = fecha.getYear()
                    age = current_year - year
                    age_string = "Tienes ${age} años"
                    println(age_string)
                }
            }
        }
        stage("SECOND STAGE")
        {
            steps
            {
                script
                {
                    println("Creando archivo...")
                    full_path = path + "\\" + filename
                    writeFile(file=full_path, content=age_string)
                }
            }
        }
    }
}
