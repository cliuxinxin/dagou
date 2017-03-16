<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class group extends Model
{
    //
    protected $guarded = [];

    /**
     * A group has many group details
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function groupDetails()
    {
        return $this->hasMany('App\GroupDetail');
    }
}
