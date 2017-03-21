<?php

namespace App;

use Carbon\Carbon;
use Illuminate\Database\Eloquent\Model;
use App\User;

class Book extends Model
{
    //
    protected $guarded = [];

    /**
     *
     * Book belongs to a user
     *
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function user()
    {
        return $this->belongsTo('App\User');
    }

    /**
     * Book has many lending record
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function lendingRecords()
    {
        return $this->hasMany('App\LendingRecord');
    }

    /**
     *
     * User's name who lended the book
     *
     * @return mixed
     */
    public function lendedUserName()
    {
        return $this->lendedUser()->name;
    }

    /**
     * User lended date
     *
     * @return static
     */
    public function lendedDate()
    {
        $date = $this->latestLendingRecrod()->start_at;

        return Carbon::createFromFormat('Y-m-d H:i:s', $date);
    }
    /**
     *
     * The latest lending record
     *
     * @return mixed
     */
    public function latestLendingRecrod()
    {
        return $this->lendingRecords->sortByDesc('start_at')->first();
    }

    /**
     *
     * User who lended the book
     *
     * @return mixed
     */
    public function lendedUser()
    {
        return $this->latestLendingRecrod()->user;
    }

    /**
     *
     * Is the book owned by the user
     *
     * @param \App\User $user
     * @return bool
     */
    public function isOwnedByUser(User $user)
    {
        return $this->getAttribute('user_id') == $user->id;
    }

    public function lendingRecordsCount()
    {
        return $this->lendingRecords->count();
    }

}
