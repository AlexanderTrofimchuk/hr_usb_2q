using { hr_usb_2qModel as my } from '../db/schema.cds';

@path : '/service/hr_usb_2qService'
service hr_usb_2qService
{
    entity JobDescriptions as
        projection on my.JobDescriptions;

    entity Keywords as
        projection on my.Keywords;

    entity Candidates as
        projection on my.Candidates;

}

//annotate hr_usb_2qService with @requires :
//[
//    'authenticated-user'
//];
