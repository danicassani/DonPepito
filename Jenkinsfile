year = 1995
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
                    println("Tienes ${age} años")
                }
            }
        }
    }
}
