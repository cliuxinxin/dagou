<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Item extends Model
{
    //
    /**
     * Hospital
     *
     * @param $query
     * @return mixed
     */
    public function scopeHospital($query)
    {
        return $query->where('name','LIKE','医院')->orWhere('name','LIKE','%设备%')->orWhere('name','LIKE','%竞争%')->orWhere('name','LIKE','%CT%');
    }
}
